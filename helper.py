def print_ex(n, name, topgap=True):
    DASHLEN = 30
    BOTTOMLEN = DASHLEN * 2 + (len(str(n)) + 2)
    if topgap: print()
    print('-' * DASHLEN + ' ' + str(n) + ' ' + '-' * DASHLEN)
    print(' ' * int((BOTTOMLEN - len(name)) / 2), name)
    print('-' * BOTTOMLEN)