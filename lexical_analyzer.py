
import table_tokens

import add_lex
import add_idn
import add_con
import next_char
import symbols_classes
import re


ch = ' '
lex = ''
state = 1
hasToRead = True

collection_records_lexem = []
collection_records_idn = []
collection_records_con = []

is_goto = False

file = open('example.txt')

current_line = 1

while(True):
    if state == 1:
           if hasToRead:
               ch = next_char.next_char(file)
           while symbols_classes.white_separator(ch):
                # current_line = next_char.what_is_line(current_line, ch)
                ch = next_char.next_char(file)
           lex = ''
           if symbols_classes.letter(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 2
           elif symbols_classes.number(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 3
           elif symbols_classes.plus(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 6
           elif symbols_classes.dot(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 4
           elif symbols_classes.single_character_splitters(ch):
               lex += ch
               hasToRead = True

               if(ch == '\n'):
                    add_lex.addLex(collection_records_lexem, current_line, '\\n', table_tokens.getCode(lex))
               else:
                   add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))

               current_line = next_char.what_is_line(current_line, ch)

               state = 1
           elif symbols_classes.less(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 7
           elif symbols_classes.more(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 8
           elif symbols_classes.equally(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 9
           elif symbols_classes.exclamation(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 10
           elif symbols_classes.dollar(ch):
               lex += ch
               ch = next_char.next_char(file)
               state = 11
           else:
               if ch:
                 print("Your symbol '{symbol}' on line {line} is not valid".format(symbol = ch, line = current_line))
               file.close()
               break

    elif state == 2:
        if  symbols_classes.letter(ch) or symbols_classes.number(ch):
            state = 2
            lex += ch
            ch = next_char.next_char(file)
        else:
            if not table_tokens.getCode(lex):
                code_idn = add_idn.findIDN(lex, collection_records_idn)
                if not code_idn:
                    current_code_idn = len(collection_records_idn)

                    type_idn = add_lex.find_type_idn(collection_records_lexem, lex)
                    if type_idn:
                        add_lex.addLex(collection_records_lexem, current_line, lex, 100, current_code_idn + 1)
                        add_idn.add_idn(collection_records_idn, current_code_idn + 1, lex, type_idn)
                    else:
                        print("You use not defined identificator {id} on line {line}".format(id = lex, line = current_line))
                        file.close()
                        break


                    # add_lex.addLex(collection_records_lexem, current_line, lex, 100, current_code_idn + 1)
                    # add_idn.add_idn(collection_records_idn, current_code_idn + 1, lex, add_lex.findTypeIDN(collection_records_lexem, lex))
                else:
                    type_idn = add_lex.find_type_idn(collection_records_lexem, lex)
                    if type_idn:
                        print('You duplicate variable {var} on line {line}'.format(var = lex, line = current_line))
                        break
                    else:
                        add_lex.addLex(collection_records_lexem, current_line, lex, 100, code_idn)
            else:
                if lex == 'goto':
                    is_goto = True
                add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = False
            state = 1


    elif state == 3:
        if symbols_classes.number(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 3
        elif symbols_classes.dot(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 5
        else:
            add_lex.addLex(collection_records_lexem, current_line, lex, 101, code_con = len(collection_records_con)+1)
            add_con.add_con(collection_records_con, len(collection_records_con)+1, lex, add_con.type_con(lex))
            state = 1
            hasToRead = False


    elif state == 4:
        if symbols_classes.number(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 5
        else:
            print('You have not entered the fractional part of the constant. line = ', current_line)
            break


    elif state == 5:
        if symbols_classes.number(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 5
        else:
            add_lex.addLex(collection_records_lexem, current_line, lex, 101, code_con=len(collection_records_con) + 1)
            add_con.add_con(collection_records_con, len(collection_records_con) + 1, lex, add_con.type_con(lex))
            state = 1
            hasToRead = False


    elif state == 6:
        if collection_records_lexem[len(collection_records_lexem) - 1].code_lexem == 101 or collection_records_lexem[len(collection_records_lexem) - 1].code_lexem == 100 or collection_records_lexem[len(collection_records_lexem) - 1].code_lexem == 25:
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            state = 1
            hasToRead = False
        elif symbols_classes.number(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 3
        elif symbols_classes.dot(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 4
        else:
            print('You have not entered a constant on line {line}'.format(line = current_line))
            break


    elif state == 7:
        if symbols_classes.less(ch):
            lex += ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
        elif symbols_classes.equally(ch):
            lex =+ ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
        else:
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = False
        state = 1


    elif state == 8:
        if symbols_classes.more(ch):
            lex += ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
        elif symbols_classes.equally(ch):
            lex = + ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
        else:
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = False
        state = 1

    elif state == 9:
        if symbols_classes.equally(ch):
            lex += ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
        else:
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = False
        state = 1

    elif state == 10:
        if symbols_classes.equally(ch):
            lex += ch
            add_lex.addLex(collection_records_lexem, current_line, lex, table_tokens.getCode(lex))
            hasToRead = True
            state = 1
        else:
            print('Error. You must enter != on line {line}'.format(line = current_line))
            break

    elif state == 11:
        if symbols_classes.letter(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 12
        else:
            print('Error label')
            break

    elif state == 12:
        if symbols_classes.letter(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 12
        elif symbols_classes.number(ch):
            lex += ch
            ch = next_char.next_char(file)
            state = 12
        else:
            code_idn = add_idn.findIDN(lex, collection_records_idn)
            if not code_idn and not is_goto and ch == ':':
                current_code_idn = len(collection_records_idn)
                add_lex.addLex(collection_records_lexem, current_line, lex, 102, current_code_idn + 1)
                add_idn.add_idn(collection_records_idn, current_code_idn + 1, lex, 'LABEL')
            elif not code_idn and (is_goto or not ch == ':'):
                print('You use not defined label on line {line}'.format(line = current_line))
                break
            elif code_idn and not is_goto and ch == ':':
                print('You duplicate label {label} on line {line}'.format(label = lex, line=current_line))
                break
            else:
                add_lex.addLex(collection_records_lexem, current_line, lex, 102, code_idn)
            hasToRead = False
            state = 1

    else:
        print('Error')



add_lex.showLexes(collection_records_lexem)

add_idn.show_idn(collection_records_idn)

add_con.show_con(collection_records_con)


add_lex.write(collection_records_lexem)

add_idn.write(collection_records_idn)

add_con.write(collection_records_con)












