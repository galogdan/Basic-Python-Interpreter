# Basic-Python-Interpreter


BNF:

program ::= program statement | %empty
<statement> ::= <if_statement>
            | <while_statement>
            | <assign_statement>
            | <expr>

<if_statement> ::= 'IF' '(' <expr> ')' '{' <block> '}'  'ELSE' '{' <block> '}' 

<while_statement> ::= 'WHILE' '(' <expr> ')' '{' <block> '}'

<assign_statement> ::= <variable> '=' <expr>

<expr> ::= <term> (('+' | '-') <term>)* | <relational_expr>

<relational_expr> ::= <term> (('>' | '<' | '==') <term>)*

<term> ::= <factor> (('*' | '/') <factor>)*

<factor> ::= '(' <expr> ')'
         | <number>
         | <variable>

<block> ::= <statement>*

<number> ::= <NUMBER>

<variable> ::= <VARIABLE>

<tokens> ::= (TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE,
            TokenType.LPAREN, TokenType.RPAREN, TokenType.LBARCK, TokenType.RBRACK,
            TokenType.LINE, TokenType.NUMBER, TokenType.VARIABLE,
            TokenType.IF, TokenType.ELSE, TokenType.WHILE, TokenType.GREATER,
            TokenType.LESS, TokenType.EQUAL, TokenType.ASSIGN, TokenType.EOF)
