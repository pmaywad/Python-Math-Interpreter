from dataclasses import dataclass

@dataclass
class NumNode:
    num : float

    def __repr__(self):
        return f"{self.num}"

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