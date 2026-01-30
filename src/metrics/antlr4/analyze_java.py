from antlr4 import *
from src.metrics.antlr4.generated.JavaLexer import JavaLexer
from src.metrics.antlr4.generated.JavaParser import JavaParser
from src.metrics.antlr4.generated.JavaParserVisitor import JavaParserVisitor
from src.metrics.antlr4.generated.JavaParserListener import JavaParserListener

from src.metrics.antlr4.generated.Java8Lexer import Java8Lexer
from src.metrics.antlr4.generated.Java8Parser import Java8Parser
from src.metrics.antlr4.generated.Java8ParserListener import Java8ParserListener

from src.metrics.antlr4.generated.JavaPParser import JavaPParser
from src.metrics.antlr4.generated.JavaPParserListener import JavaPParserListener

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

OPERATOR_TOKEN_TYPES_JAVA8 = {
    Java8Lexer.ADD: "+",
    Java8Lexer.SUB: "-",
    Java8Lexer.MUL: "*",
    Java8Lexer.DIV: "/",
    Java8Lexer.ASSIGN: "=",
    Java8Lexer.EQUAL: "==",
    Java8Lexer.AND: "&&",
    Java8Lexer.OR: "||",
    Java8Lexer.INC: "++",
    Java8Lexer.DEC: "--",
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
        operators_count_per_line = defaultdict(lambda: defaultdict(int))
        for token in self.stream.tokens:
            if token.channel != Token.DEFAULT_CHANNEL:
                continue
            if token.type in OPERATOR_TOKEN_TYPES:
                operators_count_per_line[token.line][OPERATOR_TOKEN_TYPES[token.type]] += 1
        return dict(operators_count_per_line)

class JavaPAnalyzer :
    def __init__(self, java_source_code: str):
        self.lexer = JavaLexer(InputStream(java_source_code))
        self.stream = CommonTokenStream(self.lexer)
        self.parser = JavaPParser(self.stream)        

    def analyze(self, listener):
        # Implement analysis logic here        
        walker = ParseTreeWalker()
        tree = self.parser.compilationUnit()
        walker.walk(listener, tree)
        return listener
    
    def get_operator_count_per_line(self):
        self.stream.fill()
        operators_count_per_line = defaultdict(lambda: defaultdict(int))
        for token in self.stream.tokens:
            if token.channel != Token.DEFAULT_CHANNEL:
                continue
            if token.type in OPERATOR_TOKEN_TYPES:
                operators_count_per_line[token.line][OPERATOR_TOKEN_TYPES[token.type]] += 1
        return dict(operators_count_per_line)        

class Java8Analyzer :
    def __init__(self, java_source_code: str):
        self.lexer = Java8Lexer(InputStream(java_source_code))
        self.stream = CommonTokenStream(self.lexer)
        self.parser = Java8Parser(self.stream)        

    def analyze(self, listener):
        # Implement analysis logic here        
        walker = ParseTreeWalker()
        tree = self.parser.compilationUnit()
        walker.walk(listener, tree)
        return listener
    
    def get_operator_count_per_line(self):
        self.stream.fill()
        operators_count_per_line = defaultdict(lambda: defaultdict(int))
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
        #print(f"Literal found at line {ctx.start.line}: {ctx.getText()}")
        pass
    
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodCallExpression(self, ctx: JavaParser.MethodCallExpressionContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    
# print(JavaLexer.symbolicNames)

class basePListener(JavaPParserListener):
    def __init__(self):        
        # Initialize any required data structures here
        self.literal_count_per_line = defaultdict(int)
        self.method_call_count_per_line = defaultdict(int)
        
    def get_literal_count_per_line(self):
        return dict(self.literal_count_per_line)

    def get_method_call_count_per_line(self):
        return dict(self.method_call_count_per_line)

    # Override listener methods to capture relevant information
    def enterLiteral(self, ctx:JavaPParser.LiteralContext):
        self.literal_count_per_line[ctx.start.line] += 1
        #print(f"Literal found at line {ctx.start.line}: {ctx.getText()}")
        pass
    
    def enterMethodCall(self, ctx: JavaPParser.MethodCallContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodCallExpression(self, ctx: JavaPParser.MethodCallExpressionContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass


class base8Listener(Java8ParserListener):
    def __init__(self):        
        # Initialize any required data structures here
        self.literal_count_per_line = defaultdict(int)
        self.method_call_count_per_line = defaultdict(int)
        
    def get_literal_count_per_line(self):
        return dict(self.literal_count_per_line)

    def get_method_call_count_per_line(self):
        return dict(self.method_call_count_per_line)

    # Override listener methods to capture relevant information
    def enterLiteral(self, ctx:Java8Parser.LiteralContext):
        self.literal_count_per_line[ctx.start.line] += 1
        #print(f"Literal found at line {ctx.start.line}: {ctx.getText()}")
        pass
    
    def enterMethodInvocation(self, ctx:Java8Parser.MethodInvocationContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodInvocation_lf_primary(self, ctx:Java8Parser.MethodInvocation_lf_primaryContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass
    
    def enterMethodInvocation_lfno_primary(self, ctx:Java8Parser.MethodInvocation_lfno_primaryContext):
        self.method_call_count_per_line[ctx.start.line] += 1
        pass