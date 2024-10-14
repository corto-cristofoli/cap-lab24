from TreeLexer import TreeLexer
from TreeParser import TreeParser
# from TreeVisitor import TreeVisitor
from MyTreeVisitor import MyTreeVisitor

from antlr4 import InputStream, CommonTokenStream
import sys

# example of use of visitors to parse arithmetic expressions.
# stops when the first SyntaxError is launched.


def main():
    lexer = TreeLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = TreeParser(stream)
    # parser.int_tree_top()
    tree = parser.int_tree_top()
    print("Parsing : done.")
    visitor = MyTreeVisitor()
    is_binary_tree: bool = visitor.visit(tree)
    print("Is it a binary tree ? " + str(is_binary_tree))


if __name__ == '__main__':
    main()
