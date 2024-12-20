//define a tiny grammar for arith expressions with identifiers

grammar WellFoundedParen;

full_expr: expr EOF ;

expr: '[' expr ']' expr
    | '(' expr ')' expr
    |
    ;

CHAR : ~[()[\]] -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
