

def next_char(file_name):
    ch = file_name.read(1)
    if not ch:
        return ''
    return ch

def what_is_line(current_line, symbol):
    if symbol == '\n':
        return current_line + 1
    return current_line