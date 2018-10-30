
import re


def white_separator(symbol):
    if symbol == ' ' or symbol == '\v' or symbol == '\t':
        return True
    return False



def letter(symbol):
    if re.match(r'[a-z]', symbol):
        return True
    return False


def number(symbol):
    if re.match(r'[0-9]', symbol):
        return True
    return False

def plus(symbol):
    if re.match(r'[+-]', symbol):
        return True
    return False

def dot(symbol):
    if symbol == '.':
        return True
    return False

def single_character_splitters(symbol):
    if re.match(r'[,/*:{}()]', symbol) or symbol == '\n':
        return True
    return False

def less(symbol):
    if symbol == '<':
        return True
    return False

def more(symbol):
    if symbol == '>':
        return True
    return False

def equally(symbol):
    if symbol == '=':
        return True
    return False

def exclamation(symbol):
    if symbol == '!':
        return True
    return False

def dollar(symbol):
    if symbol == '$':
        return True
    return False
