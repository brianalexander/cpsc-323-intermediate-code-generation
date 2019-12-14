from enum import auto, Enum


def addBrackets(func):
    def inside(self):
        self.chain.append('<')
        func(self)
        self.chain.append('>')
        return self
    return inside


class ProductionFactory():
    def __init__(self, production_chain=None):
        if production_chain is not None:
            self.chain = production_chain

        self.chain = []

    @property
    def Finish(self):
        result = ''.join(self.chain)
        self.chain = []
        return result

    @property
    def To(self):
        self.chain.append(' -> ')
        return self

    @property
    @addBrackets
    def Statement(self):
        self.chain.append('Statement')
        return self

    @property
    @addBrackets
    def MoreStatements(self):
        self.chain.append('MoreStatements')
        return self

    @property
    @addBrackets
    def Conditional(self):
        self.chain.append('Conditional')
        return self

    @property
    @addBrackets
    def ConditionalPrime(self):
        self.chain.append('ConditionalPrime')
        return self

    @property
    @addBrackets
    def Declarative(self):
        self.chain.append('Declarative')
        return self

    @property
    @addBrackets
    def Type(self):
        self.chain.append('Type')
        return self

    @property
    @addBrackets
    def Id(self):
        self.chain.append('Id')
        return self

    @property
    @addBrackets
    def MoreIds(self):
        self.chain.append('MoreIds')
        return self

    @property
    @addBrackets
    def Relop(self):
        self.chain.append('Relop')
        return self

    @property
    @addBrackets
    def Expression(self):
        self.chain.append('Expression')
        return self

    @property
    @addBrackets
    def Assignment(self):
        self.chain.append('Assignment')
        return self

    @property
    @addBrackets
    def ExpressionPrime(self):
        self.chain.append('ExpressionPrime')
        return self

    @property
    @addBrackets
    def Term(self):
        self.chain.append('Term')
        return self

    @property
    @addBrackets
    def TermPrime(self):
        self.chain.append('TermPrime')
        return self

    @property
    @addBrackets
    def Factor(self):
        self.chain.append('Factor')
        return self

    @property
    @addBrackets
    def Begin(self):
        self.chain.append('Begin')
        return self

    @property
    @addBrackets
    def If(self):
        self.chain.append('If')
        return self

    @property
    @addBrackets
    def Then(self):
        self.chain.append('Then')
        return self

    @property
    @addBrackets
    def Else(self):
        self.chain.append('Else')
        return self

    @property
    @addBrackets
    def Endif(self):
        self.chain.append('Endif')
        return self

    @property
    @addBrackets
    def While(self):
        self.chain.append('While')
        return self

    @property
    @addBrackets
    def Do(self):
        self.chain.append('Do')
        return self

    @property
    @addBrackets
    def Whileend(self):
        self.chain.append('Whileend')
        return self

    @property
    @addBrackets
    def End(self):
        self.chain.append('End')
        return self

    @property
    @addBrackets
    def GreaterThan(self):
        self.chain.append('GreaterThan')
        return self

    @property
    @addBrackets
    def GreaterThanEqual(self):
        self.chain.append('GreaterThanEqual')
        return self

    @property
    @addBrackets
    def LessThan(self):
        self.chain.append('LessThan')
        return self

    @property
    @addBrackets
    def LessThanEqual(self):
        self.chain.append('LessThanEqual')
        return self

    @property
    @addBrackets
    def Equalequal(self):
        self.chain.append('Equalequal')
        return self

    @property
    @addBrackets
    def Notequal(self):
        self.chain.append('Notequal')
        return self

    @property
    @addBrackets
    def Int(self):
        self.chain.append('Int')
        return self

    @property
    @addBrackets
    def Float(self):
        self.chain.append('Float')
        return self

    @property
    @addBrackets
    def Bool(self):
        self.chain.append('Bool')
        return self

    @property
    @addBrackets
    def Semicolon(self):
        self.chain.append('Semicolon')
        return self

    @property
    @addBrackets
    def Comma(self):
        self.chain.append('Comma')
        return self

    @property
    @addBrackets
    def Num(self):
        self.chain.append('Num')
        return self

    @property
    @addBrackets
    def LeftParenthesis(self):
        self.chain.append('LeftParenthesis')
        return self

    @property
    @addBrackets
    def RightParenthesis(self):
        self.chain.append('RightParenthesis')
        return self

    @property
    @addBrackets
    def EOF(self):
        self.chain.append('EOF')
        return self

    @property
    @addBrackets
    def Addition(self):
        self.chain.append('Addition')
        return self

    @property
    @addBrackets
    def Subtraction(self):
        self.chain.append('Subtraction')
        return self

    @property
    @addBrackets
    def Multiplication(self):
        self.chain.append('Multiplication')
        return self

    @property
    @addBrackets
    def Division(self):
        self.chain.append('Division')
        return self

    @property
    @addBrackets
    def Assignequals(self):
        self.chain.append('Assignequals')
        return self

    @property
    @addBrackets
    def Epsilon(self):
        self.chain.append('Epsilon')
        return self


p = ProductionFactory()

INDEX_TO_RULES = [
    p.Statement.To.Epsilon.Finish,
    p.Statement.To.Assignment.Finish,
    p.Statement.To.Declarative.Finish,
    p.Statement.To.If.Conditional.Then.Statement.Else.Statement.Endif.Finish,
    p.Statement.To.While.Conditional.Do.Statement.Whileend.Finish,
    p.Statement.To.Begin.MoreStatements.End.Finish,
    p.MoreStatements.To.Statement.MoreStatements.Finish,
    p.MoreStatements.To.Epsilon.Finish,
    p.Conditional.To.Expression.ConditionalPrime.Finish,
    p.ConditionalPrime.To.Relop.Expression.Finish,
    p.ConditionalPrime.To.Epsilon.Finish,
    p.Declarative.To.Type.Id.MoreIds.Semicolon.Finish,
    p.Type.To.Int.Finish,
    p.Type.To.Float.Finish,
    p.Type.To.Bool.Finish,
    p.MoreIds.To.Comma.Id.MoreIds.Finish,
    p.MoreIds.To.Epsilon.Finish,
    p.Assignment.To.Id.Assignequals.Conditional.Semicolon.Finish,
    p.Relop.To.GreaterThan.Finish,
    p.Relop.To.LessThan.Finish,
    p.Relop.To.GreaterThanEqual.Finish,
    p.Relop.To.LessThanEqual.Finish,
    p.Relop.To.Equalequal.Finish,
    p.Relop.To.Notequal.Finish,
    p.Expression.To.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Addition.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Subtraction.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Epsilon.Finish,
    p.Term.To.Factor.TermPrime.Finish,
    p.TermPrime.To.Multiplication.Factor.TermPrime.Finish,
    p.TermPrime.To.Division.Factor.TermPrime.Finish,
    p.TermPrime.To.Epsilon.Finish,
    p.Factor.To.LeftParenthesis.Expression.RightParenthesis.Finish,
    p.Factor.To.Id.Finish,
    p.Factor.To.Num.Finish
]


class Terminals(Enum):
    BEGIN = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    ENDIF = auto()
    WHILE = auto()
    DO = auto()
    WHILEEND = auto()
    END = auto()
    GT = auto()
    LT = auto()
    GTE = auto()
    LTE = auto()
    EQUALEQUALS = auto()
    NOTEQUAL = auto()
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    SEMICOLON = auto()
    COMMA = auto()
    ID = auto()
    NUM = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    EOF = auto()
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    ASSIGNEQUALS = auto()
    EPSILON = auto()


class NonTerminals(Enum):
    STATEMENT = auto()
    MORESTATEMENTS = auto()
    CONDITIONAL = auto()
    CONDITIONAL_PRIME = auto()
    DECLARATIVE = auto()
    TYPES = auto()
    MOREIDS = auto()
    ASSIGNMENT = auto()
    EXPRESSION = auto()
    EXPRESSION_PRIME = auto()
    TERM = auto()
    TERM_PRIME = auto()
    FACTOR = auto()
    RELATIONAL_OPERATOR = auto()


# parse table
TABLE = {
    NonTerminals.STATEMENT: {
        Terminals.BEGIN: 5,
        Terminals.IF: 3,
        Terminals.THEN: None,
        Terminals.ELSE: 0,
        Terminals.ENDIF: 0,
        Terminals.WHILE: 4,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 2,
        Terminals.FLOAT: 2,
        Terminals.BOOL: 2,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 1,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.MORESTATEMENTS: {
        Terminals.BEGIN: 6,
        Terminals.IF: 6,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: 6,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: 7,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 6,
        Terminals.FLOAT: 6,
        Terminals.BOOL: 6,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 6,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: 7,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.CONDITIONAL: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 8,
        Terminals.NUM: 8,
        Terminals.LEFT_PAREN: 8,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.CONDITIONAL_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 10,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 10,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 9,
        Terminals.LT: 9,
        Terminals.GTE: 9,
        Terminals.LTE: 9,
        Terminals.EQUALEQUALS: 9,
        Terminals.NOTEQUAL: 9,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 10,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.DECLARATIVE: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 11,
        Terminals.FLOAT: 11,
        Terminals.BOOL: 11,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TYPES: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 12,
        Terminals.FLOAT: 13,
        Terminals.BOOL: 14,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.MOREIDS: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 16,
        Terminals.COMMA: 15,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.ASSIGNMENT: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 17,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.EXPRESSION: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 24,
        Terminals.NUM: 24,
        Terminals.LEFT_PAREN: 24,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.EXPRESSION_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 27,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 27,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 27,
        Terminals.LT: 27,
        Terminals.GTE: 27,
        Terminals.LTE: 27,
        Terminals.EQUALEQUALS: 27,
        Terminals.NOTEQUAL: 27,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 27,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: 27,
        Terminals.EOF: None,
        Terminals.ADDITION: 25,
        Terminals.SUBTRACTION: 26,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TERM: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 28,
        Terminals.NUM: 28,
        Terminals.LEFT_PAREN: 28,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TERM_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 31,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 31,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 31,
        Terminals.LT: 31,
        Terminals.GTE: 31,
        Terminals.LTE: 31,
        Terminals.EQUALEQUALS: 31,
        Terminals.NOTEQUAL: 31,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 31,
        Terminals.COMMA: None,
        Terminals.ID: 31,
        Terminals.NUM: 31,
        Terminals.LEFT_PAREN: 31,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: 31,
        Terminals.SUBTRACTION: 31,
        Terminals.MULTIPLICATION: 29,
        Terminals.DIVISION: 30,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.FACTOR: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 33,
        Terminals.NUM: 34,
        Terminals.LEFT_PAREN: 32,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.RELATIONAL_OPERATOR: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 18,
        Terminals.LT: 19,
        Terminals.GTE: 20,
        Terminals.LTE: 21,
        Terminals.EQUALEQUALS: 22,
        Terminals.NOTEQUAL: 23,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
}

RULES = {
    0: [],
    1: [NonTerminals.ASSIGNMENT],
    2: [NonTerminals.DECLARATIVE],
    3: [Terminals.IF, NonTerminals.CONDITIONAL,
        Terminals.THEN, NonTerminals.STATEMENT,
        Terminals.ELSE, NonTerminals.STATEMENT,
        Terminals.ENDIF],
    4: [Terminals.WHILE, NonTerminals.CONDITIONAL,
        Terminals.DO, NonTerminals.STATEMENT,
        Terminals.WHILEEND],
    5: [Terminals.BEGIN, NonTerminals.MORESTATEMENTS, Terminals.END],
    6: [NonTerminals.STATEMENT, NonTerminals.MORESTATEMENTS],
    7: [],
    8: [NonTerminals.EXPRESSION, NonTerminals.CONDITIONAL_PRIME],
    9: [NonTerminals.RELATIONAL_OPERATOR, NonTerminals.EXPRESSION],
    10: [],
    11: [NonTerminals.TYPES, Terminals.ID,
         NonTerminals.MOREIDS, Terminals.SEMICOLON],
    12: [Terminals.INT],
    13: [Terminals.FLOAT],
    14: [Terminals.BOOL],
    15: [Terminals.COMMA, Terminals.ID, NonTerminals.MOREIDS],
    16: [],
    17: [Terminals.ID, Terminals.ASSIGNEQUALS,
         NonTerminals.CONDITIONAL, Terminals.SEMICOLON],
    18: [Terminals.GT],
    19: [Terminals.LT],
    20: [Terminals.GTE],
    21: [Terminals.LTE],
    22: [Terminals.EQUALEQUALS],
    23: [Terminals.NOTEQUAL],
    24: [NonTerminals.TERM, NonTerminals.EXPRESSION_PRIME],
    25: [Terminals.ADDITION, NonTerminals.TERM,
         NonTerminals.EXPRESSION_PRIME],
    26: [Terminals.SUBTRACTION, NonTerminals.TERM,
         NonTerminals.EXPRESSION_PRIME],
    27: [],
    28: [NonTerminals.FACTOR, NonTerminals.TERM_PRIME],
    29: [Terminals.MULTIPLICATION, NonTerminals.FACTOR,
         NonTerminals.TERM_PRIME],
    30: [Terminals.DIVISION, NonTerminals.FACTOR,
         NonTerminals.TERM_PRIME],
    31: [],
    32: [Terminals.LEFT_PAREN, NonTerminals.EXPRESSION,
         Terminals.RIGHT_PAREN],
    33: [Terminals.ID],
    34: [Terminals.NUM]
}
