from lexer import Lexer

while True:
    text = input("calc >")
    lexer = Lexer(text)
    x = lexer.generate_tokens()
    print(list(x))