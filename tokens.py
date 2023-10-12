#The token class represents every token created from every character found.
#The below classes inherit the Token class and specify what type of Token the character is.
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    def __repr__(self):
        return str(self.value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)
        
class Operation(Token):
    def __init__(self,value):
        super().__init__("OP", value)