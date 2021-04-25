from lexer import Lexer
from parser import Parser

while True:
    text = input("calc >")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    expression = parser.parser()
    print(expression)
