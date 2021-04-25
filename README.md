# Python-Math-Interpreter
A mathematics interpreter from scratch using python which can perform basic mathematical operations. The input test is first processed by a lexer, then syntax analysis and parsing is done using parser. Finally the computation is done by the interpreter.

## Lexer
Lexer does the lexical analysis on the input text and identifies the tokens and type of each token. 

The input text 14 * 13 is grouped as tokens [NUM:14.0, MUL, NUM:13.0]. Whitespaces are ignored.

The tokens identified are then processed by the parser

## Parser
The parser checks if the sequence of tokens is valid or not and prepare a parse tree by identifying what is supposed to happen and in what order.

When parser sees NUM, MUL, NUM, it passes on that the two numbers are to be multiplied.

The parse tree is then passed to interpreter

## Interpreter
The interpreter does the intended computation as per the parse tree.



Run: python main.py or python3 main.py

e.g. output

calc >12*13-4

152.0

calc >-12

-12.0

calc >-(12*13+(4*8))

-188.0

calc >+12

12.0

calc >
