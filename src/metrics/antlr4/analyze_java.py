from antlr4 import *
from src.metrics.antlr4.generated.JavaLexer import JavaLexer
from src.metrics.antlr4.generated.JavaParser import JavaParser
from src.metrics.antlr4.generated.JavaParserVisitor import JavaParserVisitor
from src.metrics.antlr4.generated.JavaParserListener import JavaParserListener
from collections import defaultdict


OPERATOR_TOKEN_TYPES = {
    JavaLexer.ADD: "+",
    JavaLexer.SUB: "-",
    JavaLexer.MUL: "*",
    JavaLexer.DIV: "/",
    JavaLexer.ASSIGN: "=",
    JavaLexer.EQUAL: "==",
    JavaLexer.AND: "&&",
    JavaLexer.OR: "||",
    JavaLexer.INC: "++",
    JavaLexer.DEC: "--",
}


class JavaAnalyzer :
    def __init__(self, java_source_code: str):
        self.lexer = JavaLexer(InputStream(java_source_code))
        self.stream = CommonTokenStream(self.lexer)
        self.parser = JavaParser(self.stream)        

    def analyze(self, listener):
        # Implement analysis logic here        
        walker = ParseTreeWalker()
        tree = self.parser.compilationUnit()
        walker.walk(listener, tree)
        return listener
    
    def get_operator_count_per_line(self):
        self.stream.fill()
        operators_count_per_line = defaultdict(defaultdict(int))
        for token in self.stream.tokens:
            if token.channel != Token.DEFAULT_CHANNEL:
                continue
            if token.type in OPERATOR_TOKEN_TYPES:
                operators_count_per_line[token.line][OPERATOR_TOKEN_TYPES[token.type]] += 1
        return dict(operators_count_per_line)
        
    
    
class baseListener(JavaParserListener):
    def __init__(self):        
        # Initialize any required data structures here
        self.literal_count_per_line = defaultdict(int)
        self.method_call_count_per_line = defaultdict(int)
        
    def get_literal_count_per_line(self):
        return dict(self.literal_count_per_line)

    def get_method_call_count_per_line(self):
        return dict(self.method_call_count_per_line)

    # Override listener methods to capture relevant information
    def enterLiteral(self, ctx:JavaParser.LiteralContext):
        self.literal_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodCallExpression(self, ctx: JavaParser.MethodCallExpressionContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    
# print(JavaLexer.symbolicNames)