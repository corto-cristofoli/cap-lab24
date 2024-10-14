# Generated from Tree.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TreeParser import TreeParser
else:
    from TreeParser import TreeParser

# This class defines a complete generic visitor for a parse tree produced by TreeParser.

class TreeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TreeParser#top.
    def visitTop(self, ctx:TreeParser.TopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TreeParser#leaf.
    def visitLeaf(self, ctx:TreeParser.LeafContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TreeParser#node.
    def visitNode(self, ctx:TreeParser.NodeContext):
        return self.visitChildren(ctx)



del TreeParser