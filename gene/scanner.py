import re


def s_label(scanner, token):
    return ('label', token)


def s_condition(scanner, token):
    return ('condition', token[:-1])


def s_register(scanner, token):
    return ('register', int(token[1:]))


def s_int_10(scanner, token):
    return ('int', int(token, 10))


def s_int_16(scanner, token):
    return ('int', int(token, 16))


def s_int_2(scanner, token):
    return ('int', int(token, 2))


def s_operator(scanner, token):
    return ('operator', token)


def s_if(scanner, token):
    return ('if', token)


def s_cond(scanner, token):
    return ('cond', token)


def s_comment(scanner, token):
    return


def s_whitespace(scanner, token):
    return


scanner = re.Scanner([
    ('[\n \t\v,:]+', s_whitespace),
    (r'\b(r[0-9]+\b)', s_register),
    (r'\bif\b', s_if),
    (r'-?0x[0-9a-fA-F]+', s_int_16),
    (r'-?0b[01]+', s_int_2),
    (r'-?[0-9]+', s_int_10),
    (r'\b(add|addi|and|andi|call|call|jmp|ld|ldi|ret|' +
     r'ldg|mul|muli|or|ori|setg|sll|slli|sra|srai|srl|' +
     r'srli|st|sti|stg|sub|subi|xor|xori|cmp|mv|neg|nop|not)\b', s_operator),
    (r'/\*.*\*/', s_comment),
    ('(equal|not equal|greater than|less than|greater than or equal|' +
     r'overflow|not overflow|less than or equal|always|never|eq|neq|' +
     'gt|lt|gte|lte|n|v|nv)[ \t\v]*:', s_condition),
    ('[^ :0-9][^ :]*', s_label),
])
