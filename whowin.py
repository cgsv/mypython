def inorder(word):
    for i in range(len(word)-1):
        if ord(word[i]) >= ord(word[i+1]):
            return False
    return True        

def awinner(word):
    if inorder(word): return False
    for i in range(len(word)):
        if not awinner(word[:i] + word[i+1:]):
            return True
    return False

print awinner('aaaa')
print awinner('aaa')
