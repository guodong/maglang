from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.ignore(r'\s+')
        self.lexer.add('HEADER', 'header')
        self.lexer.add('STRUCT', 'struct')
        self.lexer.add('PARSER', 'parser')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
