from tokens import TokenType, Token

WHITESPACES = " \t\n"
DIGITS = "0123456789"

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACES:
                self.advance()
            if self.current_char == '.' or self.current_char in DIGITS:
                self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.ADD)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.SUB)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MUL)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character :'{self.current_char}'")

    def generate_number(self):
        decimal_count = 0
        num_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_count += 1
                if decimal_count > 1:
                    break

            num_str =+ self.current_char
            self.advance()

        if num_str.startswith('.'):
            num_str = '0' + num_str
        if num_str.endswith('.'):
            num_str = num_str + '0'

        yield Token(TokenType.NUM, float(num_str))