from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    userInput = input("HoepfnerScript: ")
    
    tokenizer = Lexer(userInput)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    tree = parser.parse()
    
    interpreter = Interpreter(tree)
    result = interpreter.interpret()
    
    print(result)