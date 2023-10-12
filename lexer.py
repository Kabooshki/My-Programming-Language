#The Lexer class is meant to use all stages in Lexical analysis.
#Firstly, it stores any potential characters it may come across as shown below.
#Then, it takes a 'text' parameter to represent the input in the shell and tokenises all characters
from tokens import *

class Lexer:
    digits = "0123456789"
    operations = "+-/*%"
    space = " "
    
    #This is the constructor for the Lexer class
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.tokens = []
        self.currentChar = self.text[self.index]
        self.token = None

    #This method is used to tokenise all the characters found in text
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
    
    #This method checks for a '.' character in a number to determine whether to keep it as an integer or change it to float
    def extract_number(self):
        number = ""
        isFloat = False
        while (self.currentChar in Lexer.digits or self.currentChar == ".") and (self.index < len(self.text)):
            if self.currentChar == ".":
                isFloat = True
            number += self.currentChar
            self.next()
        
        return Integer(number) if not isFloat else Float(number)
    
    #This method is used throughout the code, to move to the next character in the user input or 'text'
    def next(self):
        self.index += 1
        if self.index < len(self.text):
            self.currentChar = self.text[self.index]