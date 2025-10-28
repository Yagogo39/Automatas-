grammar MiniLang;

program 
    : (statement NEWLINE)* EOF
    ;

statement 
    : assign
    | print
    | ifStatement
    ;

assign 
    : ID '=' expr
    ;

print 
    : 'print' '(' expr ')'
    ;

ifStatement
    : 'if' '(' condition ')' block
    ;

block
    : '{' (statement NEWLINE)* '}'
    ;

condition
    : expr compOp expr
    ;

expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    | '(' expr ')'
    ;

compOp
    : '<' | '>' | '==' | '!=' | '<=' | '>='
    ;

// Tokens
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
