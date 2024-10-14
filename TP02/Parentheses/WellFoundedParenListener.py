# Generated from WellFoundedParen.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WellFoundedParenParser import WellFoundedParenParser
else:
    from WellFoundedParenParser import WellFoundedParenParser

# This class defines a complete listener for a parse tree produced by WellFoundedParenParser.
class WellFoundedParenListener(ParseTreeListener):

    # Enter a parse tree produced by WellFoundedParenParser#full_expr.
    def enterFull_expr(self, ctx:WellFoundedParenParser.Full_exprContext):
        pass

    # Exit a parse tree produced by WellFoundedParenParser#full_expr.
    def exitFull_expr(self, ctx:WellFoundedParenParser.Full_exprContext):
        pass


    # Enter a parse tree produced by WellFoundedParenParser#expr.
    def enterExpr(self, ctx:WellFoundedParenParser.ExprContext):
        pass

    # Exit a parse tree produced by WellFoundedParenParser#expr.
    def exitExpr(self, ctx:WellFoundedParenParser.ExprContext):
        pass



del WellFoundedParenParser