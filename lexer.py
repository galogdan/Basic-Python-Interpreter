from tokens import Token, TokenType
from values import MAX_LENGTH


WHITESPACE = ' \n\t'
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_tokens(text):  # main tokenizing function
    text_iter = iter(text)
    current_char = next(text_iter, None)
    line = 1

    def advance():
        nonlocal current_char
        current_char = next(text_iter, None)

    def generate_number():  # build a number
        decimal_point_count = 0
        number_str = current_char
        advance()

        while current_char is not None and (current_char == '.' or current_char in DIGITS):
            if current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    raise Exception(f"Multiple decimal points")

            number_str += current_char
            advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))

    def generate_identifier():  # build variable
        identifier = ''
        while current_char is not None and (current_char in LETTERS or current_char in DIGITS or current_char == '_'):
            identifier += current_char
            advance()
        if len(identifier) > MAX_LENGTH:
            raise Exception(f"Illegal variable name")
        return Token(TokenType.VARIABLE, identifier)

    def generate_keyword():  # build keywords
        keyword = ''
        while current_char is not None and (current_char in LETTERS):
            keyword += current_char
            advance()
        return keyword

    def generate_equals():  # build = or ==
        equals = ''
        if current_char is not None and (current_char in '='):
            equals += current_char
            advance()
        if current_char is not None and (current_char in '='):
            equals += current_char
            advance()
        return equals

    while current_char is not None:

        if current_char in WHITESPACE:
            advance()
        elif current_char in DIGITS or current_char == '.':
            yield generate_number()
        elif current_char == 'i':
            keyword = generate_keyword()
            if keyword == 'if':
                yield Token(TokenType.IF)
            else:
                if len(keyword) > MAX_LENGTH:
                    raise Exception(f"Illegal variable name")
                yield Token(TokenType.VARIABLE, keyword)
        elif current_char == 'e':
            keyword = generate_keyword()
            if keyword == 'else':
                yield Token(TokenType.ELSE)
        elif current_char == '=':
            keyword = generate_equals()
            if keyword == '==':
                yield Token(TokenType.EQUAL, '==')
            else:
                yield Token(TokenType.ASSIGN, '=')
        elif current_char == 'w':
            keyword = generate_keyword()
            if keyword == 'while':
                yield Token(TokenType.WHILE)
            else:
                if len(keyword) > MAX_LENGTH:
                    raise Exception(f"Illegal variable name")
                yield Token(TokenType.VARIABLE, keyword)
        elif current_char in LETTERS:
            yield generate_identifier()
        elif current_char == '+':
            advance()
            yield Token(TokenType.PLUS)
        elif current_char == '-':
            advance()
            yield Token(TokenType.MINUS)
        elif current_char == '*':
            advance()
            yield Token(TokenType.MULTIPLY)
        elif current_char == '/':
            advance()
            yield Token(TokenType.DIVIDE)
        elif current_char == '(':
            advance()
            yield Token(TokenType.LPAREN)
        elif current_char == ')':
            advance()
            yield Token(TokenType.RPAREN)
        elif current_char == '=':
            advance()
            yield Token(TokenType.ASSIGN)
        elif current_char == '>':
            advance()
            yield Token(TokenType.GREATER, '>')
        elif current_char == '<':
            advance()
            yield Token(TokenType.LESS, '<')
        elif current_char == '{':
            advance()
            yield Token(TokenType.LBARCK)
        elif current_char == '}':
            advance()
            yield Token(TokenType.RBRACK)
        else:
            raise Exception(f"Illegal character '{current_char}' in line '{line}'")


