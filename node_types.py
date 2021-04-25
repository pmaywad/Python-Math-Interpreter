from dataclasses import dataclass

@dataclass
class NumNode:
    value : float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node_a : any
    node_b : any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubNode:
    node_a : any
    node_b : any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MulNode:
    node_a : any
    node_b : any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
    node_a : any
    node_b : any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

@dataclass
class PlusNode:
    """
    +5 ==> 5
    """
    node_a: any

    def __repr__(self):
        return f"({self.node_a})"

@dataclass
class MinusNode:
    """
    To represent unary operation - eg. -5
    """
    node_a : any

    def __repr__(self):
        return f"(-{self.node_a})"
