from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from WellFoundedParenLexer import WellFoundedParenLexer
from WellFoundedParenParser import WellFoundedParenParser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = WellFoundedParenLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = WellFoundedParenParser(stream)
    parser.full_expr()  # We want to recognize full_expr in grammar WellFoundedParen
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
