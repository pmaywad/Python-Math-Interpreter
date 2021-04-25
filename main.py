from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("calc >")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        expression = parser.parser()
        #print(expression)
        if not expression:
            continue
        interpreter = Interpreter()
        result = interpreter.visit_node(expression)
        print(result)

    except Exception as e:
        print("Error:", e)