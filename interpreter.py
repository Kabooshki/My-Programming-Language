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
            return left + right
        elif operator.value == "-":
            return left - right
        
    def interpret(self):
        left_node = self.tree[0] # Left subtree
        operator = self.tree[1] # Root node
        right_node = self.tree[2] # Right subtree
        
        return self.compute_binary_tree(left_node, operator, right_node)