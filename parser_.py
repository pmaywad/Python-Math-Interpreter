from node_types import *
from tokens import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        """
        Raises exception in case of invalid syntax
        """
        raise Exception("Invalid Syntax")

    def advance(self):
        """
        Advance to next token in the list of tokens
        """
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parser(self):
        """
        Main method to parse the syntax
        :return: parse tree
        """
        if self.current_token is None:
            return

        expr = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return expr

    def expr(self):
        """
        An expression contains of addition and subtraction of terms
        """
        result = self.term()
        while self.current_token is not None and self.current_token.type in (TokenType.ADD, TokenType.SUB):
            if self.current_token.type is TokenType.ADD:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type is TokenType.SUB:
                self.advance()
                result = SubNode(result, self.term())

        return result


    def term(self):
        """
        A term contains of multiplication and division of Number
        """
        result = self.number()
        while self.current_token is not None and self.current_token.type in (TokenType.MUL, TokenType.DIVIDE):
            if self.current_token.type is TokenType.MUL:
                self.advance()
                result = MulNode(result, self.number())
            elif self.current_token.type is TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.number())

        return result

    def number(self):
        """
        Parser to parse numbers
        """
        token = self.current_token
        if token is not None and token.type is TokenType.NUM:
            self.advance()
            return NumNode(token.value)

        self.raise_error()
