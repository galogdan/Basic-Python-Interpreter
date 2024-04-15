from nodes import *
from values import Number, Boolean, MAX_LENGTH


symbol_table = {}  # symbol table for checks
def interpret(node):

    def visit(node, visit_functions):  # the main visit function

        method_name = f'visit_{type(node).__name__}'  # choosing the method based on the node type
        method = visit_functions.get(method_name)
        if method:
            return method(node, visit_functions)
        else:
            raise Exception(f"No {method_name} method defined")

    def visit_NumberNode(node, visit_functions):
        return Number(node.value)

    def visit_AddNode(node, visit_functions):
        return Number(visit(node.node_a, visit_functions).value + visit(node.node_b, visit_functions).value)

    def visit_SubtractNode(node, visit_functions):
        return Number(visit(node.node_a, visit_functions).value - visit(node.node_b, visit_functions).value)

    def visit_MultiplyNode(node, visit_functions):
        return Number(visit(node.node_a, visit_functions).value * visit(node.node_b, visit_functions).value)

    def visit_DivideNode(node, visit_functions):
        try:
            return Number(visit(node.node_a, visit_functions).value / visit(node.node_b, visit_functions).value)
        except ZeroDivisionError:
            raise Exception("Division by zero is not allowed")

    def visit_VariableNode(node, visit_functions):
        if node.name in symbol_table:
            return symbol_table[node.name]
        else:
            raise Exception(f"Variable '{node.name}' is not defined")

    def visit_AssignNode(node, visit_functions):
        var_name = node.variable.name
        symbol_table[var_name] = visit(node.value, visit_functions)

    def visit_IfNode(node, visit_functions):
        condition = visit(node.condition, visit_functions)
        if condition.value:
            for statement in node.if_body:
                visit(statement, visit_functions)
        elif node.else_body:
            for statement in node.else_body:
                visit(statement, visit_functions)

    def visit_WhileNode(node, visit_functions):
        while visit(node.condition, visit_functions).value:
            for statement in node.body:
                visit(statement, visit_functions)

    def visit_GreaterThanNode(node, visit_functions):
        return Boolean(visit(node.node_a, visit_functions).value > visit(node.node_b, visit_functions).value)

    def visit_LessThanNode(node, visit_functions):
        return Boolean(visit(node.node_a, visit_functions).value < visit(node.node_b, visit_functions).value)

    def visit_EqualsNode(node, visit_functions):
        return Boolean(visit(node.node_a, visit_functions).value == visit(node.node_b, visit_functions).value)

    def visit_ProgramNode(node, visit_functions):
        for statement in node.statements:
            visit(statement, visit_functions)

    # constructing dictionary with visit functions
    visit_functions = {
        'visit_NumberNode': visit_NumberNode,
        'visit_AddNode': visit_AddNode,
        'visit_SubtractNode': visit_SubtractNode,
        'visit_MultiplyNode': visit_MultiplyNode,
        'visit_DivideNode': visit_DivideNode,
        'visit_VariableNode': visit_VariableNode,
        'visit_AssignNode': visit_AssignNode,
        'visit_IfNode': visit_IfNode,
        'visit_WhileNode': visit_WhileNode,
        'visit_GreaterThanNode': visit_GreaterThanNode,
        'visit_LessThanNode': visit_LessThanNode,
        'visit_EqualsNode': visit_EqualsNode,
        'visit_ProgramNode': visit_ProgramNode,
    }


    return visit(node, visit_functions)


