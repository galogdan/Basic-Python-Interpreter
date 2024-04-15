Running instructions:
For the interactive mode just run the main without any args.
For file mode please run the following command in terminal:
“python main.py input_file.txt” (the file name)
Make sure the input file is in the same folder as the python files.

BNF Grammar


<program>           ::=   <block> | %empty

<block> 	            ::=   <statement> <block>
                        | <statement>

<statement>             ::= <assignment_statement>
                            | <if_statement>
                            | <while_statement>
					 | <expression>

<assignment_statement>  ::= <variable> "=" <expression>

<if_statement>          ::= "if" "(" <bool_expression> ")" "{"<block>"}"
                            ["else" "{" <block> "}"]

<while_statement>     ::= "while" "(" <bool_expression> ")" "{" <block> "}"

<expression>            ::= <term> ("+" <term> | "-" <term>)* 
| <bool_expression>
<bool_expression>       ::=  <term> (">" <term> | "<" <term> | "==" <term>)

<term>                  ::= <factor> ("*" <factor> | "/" <factor>)*

<factor>                ::= <number>
                            | <variable>
                            | "(" <expression> ")"
                            | <factor>

<number>                ::= [0-9]+ | [0-9]+.[0-9]+

<variable>              ::= [a-zA-Z_]+

Syntax and Grammar Design:
1.	Minimalistic Language: Minimalistic syntax with basic constructs such as if-else, while loops, and assignment statements.
2.	Arithmetic and Relational Expressions: The language supports basic arithmetic operations (addition, subtraction, multiplication, division) and relational operations (greater than, less than, equal to).
3.	Block Structure: The language allows block structures for if and while statements, where multiple statements can be grouped within curly braces ({}).
4.	Variable Handling: The language allows the use of variables for assignment and manipulation within expressions.

Tokenization and Lexical Analysis:
1.	Token Types: The language uses predefined token types such as arithmetic operators (PLUS, MINUS, MULTIPLY, DIVIDE), relational operators (GREATER, LESS, EQUAL), control flow keywords (IF, ELSE, WHILE), and others.
2.	Token Structure: Some Tokens must have types and semantic values as necessary, e.g., TokenType.NUMBER with a numeric value or TokenType.VARIABLE with a variable name.

Parsing:
1.	Recursive Descent Parsing: This method involves recursively breaking down the input based on the grammar rules.
2.	Error Handling: The parser includes error handling for invalid syntax through the raise_error() method. This catches invalid tokens and structures, providing descriptive error messages.
3.	Lookahead Token: The parser uses a lookahead approach, keeping track of the current token and the next token, allowing for decision-making based on the next token's type.

Control Flow Constructs:
1.	If Statements: The language supports if-else constructs with a required condition and optional else block.
2.	While Loops: While loops are supported with a condition and a block of statements that can be repeated based on the condition.

Expressions and Operations:
1.	Precedence and Associativity: The language follows common mathematical precedents and associativity for arithmetic and relational expressions.
2.	Operator Types: Binary operations (addition, subtraction, multiplication, division) and relational operations (greater, less, equal) are supported.
3.	The language supports parentheses for grouping expressions.

Variables and Assignment:
1.	Variable Declarations: Variables are declared implicitly upon first use and are case-sensitive.
2.	Assignment Statements: Assignments use the = operator to assign a value to a variable.

Code Structure:
1.	Statements and Blocks: Code can be structured into statements and blocks of code. Blocks are enclosed within {} to denote scope and grouping.

Others:
1.	Type System: Dynamically typed with simple types (numbers).
 
Trade-offs & Limitations
1.	Lack of Advanced Features: The language does not support advanced language features such as classes or modules, which limits its expressiveness.
2.	Performance Considerations: Recursive descent parsing can be slower compared to other parsing techniques.
3.	No Type Inference: The language does not perform type inference (the numbers are float dynamically).

Milestones and Language Evolution
The initial implementation focuses on basic constructs for basic arithmetic and relational expressions which are supported to enable logical control flow.
After implementing the basic arithmetic we implemented the more complex statements such as if-else and while.
As we added keywords and options the BNF grew accordingly from a basic BNF of expressions to a more complex one with variables and different conditions and expressions handling.
After implementing the statements (and block of statements) we could test the interpreter and as we expected: the Lexer raising the errors of Illegal characters , the Parser raising errors referring the syntax and the Interpreter for semantic issues such as undefined variables.
