from tokens import TokenType, Token
from nodes import *


def raise_error(line):  # syntax errors handling
    raise Exception(f"Invalid syntax")


def parse(tokens):  # parse function
    tokens_iter = iter(tokens)
    line = 1

    def advance(): # advance tokens
        nonlocal line
        try:
            token = next(tokens_iter)
            return token
        except StopIteration:
            return None

    def program():
        statements = []
        while current_token is not None:
            statements.append(statement())
        return ProgramNode(statements)

    def statement():
        token = current_token

        if token.type == TokenType.IF:
            return if_statement()
        elif token.type == TokenType.WHILE:
            return while_statement()
        elif token.type == TokenType.VARIABLE:
            return assign_statement()
        else:
            return expr()

    def if_statement():
        consume(TokenType.IF)
        consume(TokenType.LPAREN)
        condition = expr()
        consume(TokenType.RPAREN)
        body = None
        if current_token.type != TokenType.LBARCK:
            raise_error(line)
        if current_token.type == TokenType.LBARCK:
            body = block()  # Parse multiple statements
        else:
            body = [statement()]  # Parse a single statement

        else_body = None
        if current_token is not None and current_token.type == TokenType.ELSE:
            consume(TokenType.ELSE)
            if current_token.type != TokenType.LBARCK:
                raise_error(line)
            if current_token.type == TokenType.LBARCK:
                else_body = block()  # Parse multiple statements in else block
            else:
                else_body = [statement()]  # Parse a single statement in else block

        return IfNode(condition, body, else_body)

    def while_statement():
        consume(TokenType.WHILE)
        consume(TokenType.LPAREN)
        condition = expr()
        consume(TokenType.RPAREN)
        body = None

        if current_token.type == TokenType.LBARCK:
            body = block()  # Parse multiple statements
        else:
            body = [statement()]  # Parse a single statement

        return WhileNode(condition, body)

    def assign_statement():
        var_name = current_token.value
        consume(TokenType.VARIABLE)
        consume(TokenType.ASSIGN)
        value = expr()
        return AssignNode(VariableNode(var_name), value)

    def expr():
        result = term()

        while current_token is not None and current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.GREATER, TokenType.LESS, TokenType.EQUAL):
            if current_token.type == TokenType.PLUS:
                consume(TokenType.PLUS)
                result = AddNode(result, term())
            elif current_token.type == TokenType.MINUS:
                consume(TokenType.MINUS)
                result = SubtractNode(result, term())
            elif current_token.type == TokenType.GREATER:
                consume(TokenType.GREATER)
                result = GreaterThanNode(result, term())
            elif current_token.type == TokenType.LESS:
                consume(TokenType.LESS)
                result = LessThanNode(result, term())
            elif current_token.type == TokenType.EQUAL:
                consume(TokenType.EQUAL)
                result = EqualsNode(result, term())

        return result

    def term():
        result = factor()

        while current_token is not None and current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if current_token.type == TokenType.MULTIPLY:
                consume(TokenType.MULTIPLY)
                result = MultiplyNode(result, factor())
            elif current_token.type == TokenType.DIVIDE:
                consume(TokenType.DIVIDE)
                result = DivideNode(result, factor())

        return result

    def factor():
        token = current_token

        if token.type == TokenType.LPAREN:
            consume(TokenType.LPAREN)
            result = expr()
            consume(TokenType.RPAREN)
            return result

        elif token.type == TokenType.NUMBER:
            consume(TokenType.NUMBER)
            return NumberNode(token.value)

        elif token.type == TokenType.VARIABLE:
            var_name = token.value
            consume(TokenType.VARIABLE)
            return VariableNode(var_name)

        raise_error(line)

    def consume(token_type):  # consuming tokens
        nonlocal current_token
        if current_token is not None and current_token.type == token_type:
            current_token = advance()
        else:
            raise_error(line)

    def block():  # block of statements
        statements = []
        consume(TokenType.LBARCK)  # Consuming the opening curly brace
        while current_token is not None and current_token.type != TokenType.RBRACK:
            statements.append(statement())
        consume(TokenType.RBRACK)  # Consuming the closing curly brace
        return statements

    current_token = advance()
    return program()


