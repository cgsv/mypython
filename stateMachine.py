def commentParser(word):
    i, state = 0, 'code'
    while i < len(word):
        c = word[i]
        oState = state
        if state == 'code':
            if c == '/': state = 'slash'
        elif state == 'slash':
            if c == '*': state = 'comment'
            elif c == '/': pass
            else: state = 'code'
        elif state == 'comment':
            if c == '*': state = 'star'
        elif state == 'star':
            if c == '*': pass
            elif c == '/': state = 'code'
            else: state = 'comment'
        print c, oState, '->', state
        i += 1

if __name__ == '__main__':
    commentParser("int c = 0; /*** This is a comment **aghf*/ int d=0;")
