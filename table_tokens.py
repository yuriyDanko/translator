

def getTokens ():
    return {
        1   : 'int',
        2   : 'float',
        3   : 'repeat',
        4   : 'until',
        5   : 'if',
        6   : 'cin',
        7   : 'echo',
        8   : '{',
        9   : '}',
        10  : ',',
        11  : '=',
        12  : '<<',
        13  : '>>',
        14  : '<',
        15  : '>',
        16  : '<=',
        17  : '>=',
        18  : '==',
        19  : '!=',
        20  : '+',
        21  : '*',
        22  : '/',
        23  : '-',
        24  : '(',
        25  : ')',
        26  : 'tiger',
        27  : 'start',
        28  : 'finish',
        29  : 'goto',
        30  : ':',
        31  : '\n',
        100 : 'IDN',
        101 : 'CON',
        102 : 'LABEL'
    }

def getCode(token):
    tokens = getTokens()
    for key, val in tokens.items():
        if val == token:
            return key
    return None
