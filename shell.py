from lexer import Lexer
from parse import Parser

while True:
    userInput = input("HoepfnerScript: ")
    
    tokenizer = Lexer(userInput)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    tree = parser.parse()
    
    print(tree)