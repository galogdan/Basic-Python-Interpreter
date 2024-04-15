from dataclasses import dataclass


# using data classes to simplify the code

@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"


@dataclass
class ProgramNode:
    statements: any

    def __repr__(self):
        return '\n'.join([str(statement) for statement in self.statements])


@dataclass
class VariableNode:
    name: str

    def __repr__(self):
        return f"VariableNode({self.name})"


@dataclass
class IfNode:
    condition: any
    if_body: any
    else_body: any = None

    def __repr__(self):
        if self.else_body:
            return f"IfNode(condition={self.condition}, if_body={self.if_body}, else_body={self.else_body})"
        else:
            return f"IfNode(condition={self.condition}, if_body={self.if_body})"


@dataclass
class WhileNode:
    condition: any
    body: any

    def __repr__(self):
        return f"WhileNode(condition={self.condition}, body={self.body})"


@dataclass
class AssignNode:
    variable: any
    value: any

    def __repr__(self):
        return f"{self.variable} = {self.value}"


@dataclass
class GreaterThanNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} > {self.node_b})"


@dataclass
class LessThanNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} < {self.node_b})"


@dataclass
class EqualsNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} == {self.node_b})"
