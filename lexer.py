class Lexer:
    digits = "0123456789"
    operations = "+-/*%"
    space = " "
    
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.tokens = []
        self.currentChar = self.text[self.index]
        self.token = None

    def tokenize(self):
        while self.index < len(self.text):
            if self.currentChar in Lexer.digits:
                self.token = self.extract_number()
                
            elif self.currentChar in Lexer.operations:
                self.token = Operation(self.currentChar)
                self.next()
            
            elif self.currentChar in Lexer.space:
                self.next()
                continue
                
            self.tokens.append(self.token)
            
        return self.tokens
    
    def extract_number(self):
        number = ""
        isFloat = False
        while (self.currentChar in Lexer.digits or self.currentChar == ".") and (self.index < len(self.text)):
            if self.currentChar == ".":
                isFloat = True
            number += self.currentChar
            self.next()
        
        return Integer(number) if not isFloat else Float(number)
    
    def next(self):
        self.index += 1
        if self.index < len(self.text):
            self.currentChar = self.text[self.index]

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