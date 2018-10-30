

import lexem




def addLex(collection_records_lexem, line, lex, code, code_idn = None, code_con = None):
    collection_records_lexem.append(lexem.Lexem(len(collection_records_lexem) + 1,
                                                 line,
                                                 lex,
                                                 code,
                                                 code_idn,
                                                 code_con))

def showLexes(collection_records_lexem):
    count = len(collection_records_lexem)
    print(' ')
    print("-------------------------------------------------------------------------------------")
    print("|                                Table tokens                                       |")
    print("-------------------------------------------------------------------------------------")
    print("|  serial_number  | line_number |      lexem     | code_lexem | code_idn | code_con |")
    print("-------------------------------------------------------------------------------------")
    for i in range(0,count):
        print("|       %-4i      |      %-3i    |     %-6s     |     %-3s    |    %-4s  |   %-4s   |"%(collection_records_lexem[i].serial_number,
                                                                                                      collection_records_lexem[i].line_number,
                                                                                                      collection_records_lexem[i].lexem,
                                                                                                      collection_records_lexem[i].code_lexem,
                                                                                                      collection_records_lexem[i].code_idn,
                                                                                                      collection_records_lexem[i].code_con))
        print("-------------------------------------------------------------------------------------")


def findTypeIDN(collection_records, idn):
    serial_number = len(collection_records) - 1
    while serial_number >= 0:
        if collection_records[serial_number].lexem == 'tiger' or collection_records[serial_number].lexem == 'int' or collection_records[serial_number].lexem == 'float':
           return collection_records[serial_number].lexem
        serial_number -= 1


def find_type_idn(collection_records_lex, idn):
    index_last_lex = len(collection_records_lex) - 1
    while index_last_lex >= 0:
        if collection_records_lex[index_last_lex].lexem == 'tiger' or collection_records_lex[index_last_lex].lexem == 'int' or collection_records_lex[index_last_lex].lexem == 'float':
            return  collection_records_lex[index_last_lex].lexem
        elif collection_records_lex[index_last_lex].lexem == ',':
            if collection_records_lex[index_last_lex - 1].code_lexem == 100:
                index_last_lex -= 2
                continue
            else:
                return None
        else:
            return None


def write(collection_records_lexem):
    count = len(collection_records_lexem)
    file = open('output_lexem.txt', 'w')
    for i in range(0, count):
        file.write("       %-4i            %-3i         %-6s          %-3s        %-4s      %-4s   \n" % (
        collection_records_lexem[i].serial_number,
        collection_records_lexem[i].line_number,
        collection_records_lexem[i].lexem,
        collection_records_lexem[i].code_lexem,
        collection_records_lexem[i].code_idn,
        collection_records_lexem[i].code_con))
    file.close()




