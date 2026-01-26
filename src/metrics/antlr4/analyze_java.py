from antlr4 import *
from generated.JavaLexer import JavaLexer
from generated.JavaParser import JavaParser
from generated.JavaParserVisitor import JavaParserVisitor
from generated.JavaParserListener import JavaParserListener
from collections import defaultdict

class JavaAnalyzer :
    def __init__(self, java_source_code: str, listener):
        self.lexer = JavaLexer(InputStream(java_source_code))
        self.stream = CommonTokenStream(self.lexer)
        self.parser = JavaParser(self.stream)
        self.tree = self.parser.compilationUnit()
        self.listener = listener

    def analyze(self):
        # Implement analysis logic here
        walker = ParseTreeWalker()
        walker.walk(self.listener, self.tree)
        return self.listener
    
    
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