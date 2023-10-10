from lexer import Lexer

while True:
    userInput = input("HoepfnerScript: ")
    tokenizer = Lexer(userInput)
    tokens = tokenizer.tokenize()
    
    print(tokens)