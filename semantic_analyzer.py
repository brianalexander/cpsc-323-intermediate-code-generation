import sys
from lexer import lexer
from utilities import token_to_terminal, print_instruction_table, print_symbol_table
from Constants import Terminals

symbol_index = 0

code_listing_index = 1
code_listing = []

# stack = []
op_stack = []

# memory_table = {}

next_available_memory_location = 5000

symbol_table = {
    "identifier": [],
    "memory_location": [],
    "type": []
}


def add_symbol_to_table(identifier, memory_location, sym_type):
    global next_available_memory_location
    if(identifier not in symbol_table['identifier']):
        symbol_table['identifier'].append(identifier)
        symbol_table['memory_location'].append(memory_location)
        symbol_table['type'].append(sym_type)

        next_available_memory_location = next_available_memory_location + 1
    else:
        # TODO: ERROR
        print("Symbol", identifier, "already declared.")


def ADD():
    global code_listing_index
    code_listing.append([code_listing_index, 'ADD', None])
    code_listing_index = code_listing_index + 1

    # stack.append(stack.pop() + stack.pop())


def MUL():
    global code_listing_index
    code_listing.append([code_listing_index, 'MUL', None])
    code_listing_index = code_listing_index + 1

    # stack.append(stack.pop() * stack.pop())


def DIV():
    global code_listing_index
    code_listing.append([code_listing_index, 'DIV', None])
    code_listing_index = code_listing_index + 1

    # stack.append(stack.pop() / stack.pop())


def SUB():
    global code_listing_index
    code_listing.append([code_listing_index, 'SUB', None])
    code_listing_index = code_listing_index + 1

    # stack.append(stack.pop() - stack.pop())


def PUSHI(integer):
    global code_listing_index
    code_listing.append([code_listing_index, 'PUSHI', integer])
    code_listing_index = code_listing_index + 1
    # stack.append(int(integer))


def PUSHM(memory_address):
    global code_listing_index
    code_listing.append([code_listing_index, 'PUSHM', memory_address])
    code_listing_index = code_listing_index + 1
    # stack.append(int(integer))


def POPM(memory_address):
    global code_listing_index
    code_listing.append(
        [code_listing_index, 'POPM', memory_address])
    # memory_table[memory_address] = stack.pop()


def error(message):
    print("Syntax Error:", message)
    sys.exit(0)


def next_symbol():
    global symbol_index
    symbol_index = symbol_index + 1


def isTerminal(symbol):
    if(terminal_string[symbol_index][2] is symbol):
        return True
    return False


def accept(symbol):
    if(terminal_string[symbol_index][2] is symbol):
        next_symbol()
        return True

    return False


def expect(symbol):
    if(accept(symbol)):
        return True
    error("Encountered unexpected symbol.")  # ends execution


def Type():
    if(accept(Terminals.INT) or
       accept(Terminals.FLOAT) or
       accept(Terminals.BOOL)):
        pass
    else:
        error("Invalid type.")


def Declarative():
    sym_type = terminal_string[symbol_index][1]
    Type()
    while(True):
        sym_iden = terminal_string[symbol_index][1]
        expect(Terminals.ID)
        add_symbol_to_table(sym_iden, next_available_memory_location, sym_type)
        if(accept(Terminals.COMMA)):
            continue
        if(accept(Terminals.SEMICOLON)):
            break


def Assignment():
    print('assignment')
    sym_iden = terminal_string[symbol_index][1]

    expect(Terminals.ID)

    try:
        memory_index = symbol_table['identifier'].index(sym_iden)
    except ValueError:
        error("Identifier not declared.")

    expect(Terminals.ASSIGNEQUALS)

    op_stack.append([POPM, symbol_table['memory_location'][memory_index]])

    Conditional()
    expect(Terminals.SEMICOLON)


def Statement():
    while(True):
        print('statement')
        if(accept(Terminals.SEMICOLON)):
            continue
        elif(isTerminal(Terminals.INT) or
             isTerminal(Terminals.FLOAT) or
             isTerminal(Terminals.BOOL)):
            Declarative()
        elif(isTerminal(Terminals.ID)):
            Assignment()
            while(len(op_stack)):
                operation = op_stack.pop()
                operation[0](*operation[1:])

        if(accept(Terminals.EOF)):
            break


def Expression():
    print('expression')
    Term()
    Expression_Prime()


def Expression_Prime():
    print('expression prime')
    if(accept(Terminals.ADDITION)):
        op_stack.append([ADD])
        Term()
        Expression_Prime()
    if(accept(Terminals.SUBTRACTION)):
        op_stack.append([SUB])
        Term()
        Expression_Prime()


def Conditional():
    print('conditional')
    Expression()
    Conditional_Prime()


def Conditional_Prime():
    print('conditional prime')
    if(isTerminal(Terminals.GT) or
       isTerminal(Terminals.LT) or
       isTerminal(Terminals.GTE) or
       isTerminal(Terminals.LTE) or
       isTerminal(Terminals.EQUALEQUALS) or
       isTerminal(Terminals.NOTEQUAL)):
        Relop()
        Expression()


def Relop():
    print('relop')
    if(accept(Terminals.GT)):
        pass
    elif(accept(Terminals.LT)):
        pass
    elif(accept(Terminals.GTE)):
        pass
    elif(accept(Terminals.LTE)):
        pass
    elif(accept(Terminals.EQUALEQUALS)):
        pass
    elif(accept(Terminals.NOTEQUAL)):
        pass


def Term():
    print('term')
    Factor()
    Term_Prime()


def Term_Prime():
    print('term prime')
    if(accept(Terminals.MULTIPLICATION)):
        op_stack.append([MUL])
        Factor()
        Term_Prime()
    if(accept(Terminals.DIVISION)):
        op_stack.append([DIV])
        Factor()
        Term_Prime()


def Factor():
    print('factor')
    tmp_sym = terminal_string[symbol_index][1]

    if(accept(Terminals.LEFT_PAREN)):
        Expression()
        expect(Terminals.RIGHT_PAREN)
    elif(accept(Terminals.ID)):
        try:
            memory_index = symbol_table['identifier'].index(tmp_sym)
            PUSHM(symbol_table['memory_location'][memory_index])
        except ValueError:
            error("Identifier not declared.")
    elif(accept(Terminals.NUM)):
        PUSHI(tmp_sym)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please specify a file path to lex as the first argument.")
        sys.exit()

    # To lex a file, please pass the path as the first argument
    # Example usage: python3 lexer.py [path]
    path = sys.argv[1]

    tokens, illegal_tokens = lexer(path)

    terminal_string = token_to_terminal(tokens)
    terminal_string.append(('EOF', '$', Terminals.EOF, 0))
    print(terminal_string)

    # print(terminal_string[symbol_index])
    # print(isinstance(terminal_string[symbol_index][2], Terminals))
    # print(terminal_string[symbol_index][2] is Terminals.ID)

    Statement()
    print("input accepted")
    print_symbol_table(symbol_table)
    print('----------')
    print_instruction_table(code_listing)
    # print(stack)
    # print(op_stack)
    # print(memory_table)


# def MoreIDs():
#     if(accept(Terminals.COMMA)):
#         expect(Terminals.ID)
#         MoreIDs()
#     elif(accept(Terminals.SEMICOLON)):
#         pass

# def MoreStatements():
#     print('more statement')
#     print(terminal_string)
#     Statement()

#     # Keep looping until EOF reached
#     if(not accept(Terminals.EOF)):
#         MoreStatements()
