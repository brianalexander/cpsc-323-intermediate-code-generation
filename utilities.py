from enum import Enum, auto
from Constants import Terminals


def token_to_terminal(tokens):
    terminal_string = []
    # tokens[0] -> token
    # tokens[1] -> lexeme
    # tokens[2] -> line number
    for i in range(len(tokens)):
        to_append = []
        current_token = tokens[i][0]
        current_lexeme = tokens[i][1]

        # Add the token in position 0
        to_append.append(current_token)

        # Add the lexeme in position 1
        to_append.append(str.lower(current_lexeme))

        # Add the Terminal in position 2
        if(current_token == "KEYWORD"):
            if(current_lexeme == 'begin'):
                to_append.append(Terminals.BEGIN)
            elif(current_lexeme == 'end'):
                to_append.append(Terminals.END)
            elif(current_lexeme == 'while'):
                to_append.append(Terminals.WHILE)
            elif(current_lexeme == 'whileend'):
                to_append.append(Terminals.WHILEEND)
            elif(current_lexeme == 'do'):
                to_append.append(Terminals.DO)
            elif(current_lexeme == 'if'):
                to_append.append(Terminals.IF)
            elif(current_lexeme == 'then'):
                to_append.append(Terminals.THEN)
            elif(current_lexeme == 'else'):
                to_append.append(Terminals.ELSE)
            elif(current_lexeme == 'endif'):
                to_append.append(Terminals.ENDIF)
            elif(current_lexeme == 'int'):
                to_append.append(Terminals.INT)
            elif(current_lexeme == 'float'):
                to_append.append(Terminals.FLOAT)
            elif(current_lexeme == 'bool'):
                to_append.append(Terminals.BOOL)
        elif(current_token in ['INT', 'REAL']):
            to_append.append(Terminals.NUM)
        elif (current_token == 'IDENTIFIER'):
            to_append.append(Terminals.ID)
        elif(current_token == 'SEPARATOR'):
            if (current_lexeme == "("):
                to_append.append(Terminals.LEFT_PAREN)
            elif (current_lexeme == ")"):
                to_append.append(Terminals.RIGHT_PAREN)
            elif(current_lexeme == ','):
                to_append.append(Terminals.COMMA)
            elif(current_lexeme == ';'):
                to_append.append(Terminals.SEMICOLON)
        elif(current_token == 'OPERATOR'):
            if (current_lexeme == "+"):
                to_append.append(Terminals.ADDITION)
            elif (current_lexeme == "-"):
                to_append.append(Terminals.SUBTRACTION)
            elif(current_lexeme == '*'):
                to_append.append(Terminals.MULTIPLICATION)
            elif(current_lexeme == '/'):
                to_append.append(Terminals.DIVISION)
            elif(current_lexeme == '>'):
                to_append.append(Terminals.GT)
            elif(current_lexeme == '>='):
                to_append.append(Terminals.GTE)
            elif(current_lexeme == '<'):
                to_append.append(Terminals.LT)
            elif(current_lexeme == '<='):
                to_append.append(Terminals.LTE)
            elif(current_lexeme == '=='):
                to_append.append(Terminals.EQUALEQUALS)
            elif(current_lexeme == '='):
                to_append.append(Terminals.ASSIGNEQUALS)
            elif(current_lexeme == '<>'):
                to_append.append(Terminals.NOTEQUAL)

        # add line number in position 3
        to_append.append(tokens[i][2])
        terminal_string.append(to_append)

    return terminal_string


def print_instruction_table(instruction_table):
    print('address\tOperation\tOperand')
    for row in instruction_table:
        print("{}\t{}\t\t{}".format(*row))

def print_symbol_table(symbol_table):
    print('Identifier\tMemory Location\tType')
    num_items = len(symbol_table['identifier'])
    for index in range(num_items):
        print('{}\t\t{}\t\t{}'.format(
            symbol_table['identifier'][index],
            symbol_table['memory_location'][index],
            symbol_table['type'][index]
        ))

