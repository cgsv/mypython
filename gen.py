def getNgen(genfun, n):
    m = genfun()
    for i in xrange(n-1):
        m.next()
    return m.next()

def genOdd():
    i = 1
    while True:
        yield i
        i += 2

def genOnes():
    yield 1
    for x in genOnes():
        yield x

print getNgen(genOdd, 20)
