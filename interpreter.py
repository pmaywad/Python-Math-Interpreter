from node_types import *
from defined_values import Number


class Interpreter:

    def visit_node(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumNode(self, node):
        return Number(node.value)

    def visit_AddNode(self,node):
        return Number(self.visit_node(node.node_a).value + self.visit_node(node.node_b).value)

    def visit_SubNode(self,node):
        return Number(self.visit_node(node.node_a).value - self.visit_node(node.node_b).value)

    def visit_MulNode(self,node):
        return Number(self.visit_node(node.node_a).value * self.visit_node(node.node_b).value)

    def visit_DivideNode(self,node):
        try:
            return Number(self.visit_node(node.node_a).value / self.visit_node(node.node_b).value)
        except:
            print("Math error")

    def visit_PlusNode(self, node):
        return self.visit_node(node.node_a)

    def visit_MinusNode(self, node):
        return Number(-(self.visit_node(node.node_a).value))
