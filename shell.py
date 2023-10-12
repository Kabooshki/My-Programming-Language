from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    userInput = input("HoepfnerScript: ")
    
    tokenizer = Lexer(userInput)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    tree = parser.parse()
    
    Interpreter = Interpreter(tree)
    result = Interpreter.interpret()
    
    print(result)