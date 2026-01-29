import sys
from antlr4 import *

class JavaParserBase(Parser):
    def __init__(self, input, output=sys.stdout):
        super().__init__(input, output)

    def DoLastRecordComponent(self) -> bool:
        # self._ctx は現在の ParserRuleContext です
        ctx = self._ctx
        
        # 循環参照を避けるため、クラス名（文字列）で型を確認します
        if type(ctx).__name__ != "RecordComponentListContext":
            return True

        # Java: tctx.recordComponent()
        # Python ANTLR4では、同名のルールが複数ある場合リストを返します
        # メソッド名は通常小文字で生成されますが、文法に合わせる必要があります
        try:
            rcs = ctx.recordComponent()
        except AttributeError:
            # メソッド名が文法ファイルにより異なる場合への対策
            return True

        if not rcs or len(rcs) == 0:
            return True

        count = len(rcs)
        for i in range(count):
            rc = rcs[i]
            # ELLIPSIS() が存在するか（Noneでないか）を確認
            if rc.ELLIPSIS() is not None and (i + 1) < count:
                return False
        return True

    def IsNotIdentifierAssign(self) -> bool:
        # self._input (TokenStream) から次のトークンを確認
        la1 = self._input.LA(1)
        
        # Javaのswitch文に相当する処理
        # self.IDENTIFIER 等は、実行時に JavaParser インスタンスから属性として取得されます
        identifiers = [
            self.IDENTIFIER, self.MODULE, self.OPEN, self.REQUIRES, 
            self.EXPORTS, self.OPENS, self.TO, self.USES, 
            self.PROVIDES, self.WHEN, self.WITH, self.TRANSITIVE, 
            self.YIELD, self.SEALED, self.PERMITS, self.RECORD, self.VAR
        ]
        
        # もし最初のトークンが識別子関連でなければ、
        # "identifier = ..." の形にはなり得ないので True を返す
        if la1 not in identifiers:
            return True
            
        # 2つ目のトークンが '=' (ASSIGN) かどうかを確認
        la2 = self._input.LA(2)
        return la2 != self.ASSIGN