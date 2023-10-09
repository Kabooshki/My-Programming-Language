class Lexer:
    digits = "0123456789"
    
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.tokens = []
        self.currentChar = self.text[self.index]
        self.token = None

        def tokenise(self):
            while self.index < len(self.text):
                if self.currentChar in Lexer.digits:
                    self.token = self.extract_number()
        
        def extract_number(self):
            number = ""
            isFloat = False
            while (self.currentChar in Lexer.digits or self.currentChar == ".") and (self.index < len(self.text)):
                if self.currentChar == ".":
                    isFloat = True
                number += self.currentChar
                self.next()
            
            return Integer("INT", number)
        
        def next(self):
            if self.index < len(self.text):
                self.currentChar = self.text[self.index]

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    pass