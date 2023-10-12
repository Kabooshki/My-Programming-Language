class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]
    
    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        
    def term(self):
        left_node = self.factor()
        self.next()
        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.next()
            right_node = self.factor()
            self.next()
            left_node = [left_node, operation, right_node]
        return left_node
    
    def expression(self):
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.next()
            right_node = self.term()
            left_node = [left_node, operation, right_node]
        return left_node

    def parse(self):
        return self.expression()

    def next(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]