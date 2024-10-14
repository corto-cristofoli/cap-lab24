# Generated from Tree.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TreeParser import TreeParser
else:
    from TreeParser import TreeParser

# This class defines a complete listener for a parse tree produced by TreeParser.
class TreeListener(ParseTreeListener):

    # Enter a parse tree produced by TreeParser#top.
    def enterTop(self, ctx:TreeParser.TopContext):
        pass

    # Exit a parse tree produced by TreeParser#top.
    def exitTop(self, ctx:TreeParser.TopContext):
        pass


    # Enter a parse tree produced by TreeParser#leaf.
    def enterLeaf(self, ctx:TreeParser.LeafContext):
        pass

    # Exit a parse tree produced by TreeParser#leaf.
    def exitLeaf(self, ctx:TreeParser.LeafContext):
        pass


    # Enter a parse tree produced by TreeParser#node.
    def enterNode(self, ctx:TreeParser.NodeContext):
        pass

    # Exit a parse tree produced by TreeParser#node.
    def exitNode(self, ctx:TreeParser.NodeContext):
        pass



del TreeParser