from tokens import *

class Interpreter:
    def __init__(self, tree):
        self.tree = tree
        
    def readINT(self, value):
        return int(value)
        
    def readFLT(self, value):
        return float(value)
        
    def compute_binary_tree(self, left, operator, right):
        # if left.type == "INT":
        #     left = int(left.value)
        # elif left.type == "FLT":
        #     left = float(left.value)
        # if right.type == "INT":
        #     right = int(right.value)
        # elif right.type == "FLT":
        #     right = float(right.value)
        left_type = left.type
        right_type = right.type
        
        left = getattr(self, f"read{left_type}")(left.value)
        right = getattr(self, f"read{right_type}")(right.value)
            
        if operator.value == "+":
            output = left + right
        elif operator.value == "-":
            output = left - right
        elif operator.value == "/":
            output = left / right
        elif operator.value == "*":
            output = left * right
        
        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)
    
        
    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree
            
        left_node = tree[0] # Left subtree
        #Check if left_node is actually a subtree or a value
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)
        
        operator = tree[1] # Root node
        
        right_node = tree[2] # Right subtree
        #Check if right_node is also actually a subtree or a value
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)
        
        return self.compute_binary_tree(left_node, operator, right_node)