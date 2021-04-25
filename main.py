from lexer import Lexer
from parser_ import Parser

while True:
    try:
        text = input("calc >")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        expression = parser.parser()
        print(expression)
    except Exception as e:
        print("Error:", e)