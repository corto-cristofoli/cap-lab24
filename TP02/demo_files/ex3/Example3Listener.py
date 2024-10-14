# Generated from Example3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Example3Parser import Example3Parser
else:
    from Example3Parser import Example3Parser

# This class defines a complete listener for a parse tree produced by Example3Parser.
class Example3Listener(ParseTreeListener):

    # Enter a parse tree produced by Example3Parser#full_expr.
    def enterFull_expr(self, ctx:Example3Parser.Full_exprContext):
        pass

    # Exit a parse tree produced by Example3Parser#full_expr.
    def exitFull_expr(self, ctx:Example3Parser.Full_exprContext):
        pass


    # Enter a parse tree produced by Example3Parser#expr.
    def enterExpr(self, ctx:Example3Parser.ExprContext):
        pass

    # Exit a parse tree produced by Example3Parser#expr.
    def exitExpr(self, ctx:Example3Parser.ExprContext):
        pass



del Example3Parser