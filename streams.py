def stream_map(func, stream):
    while True:
        yield func(stream.next())

def stream_filter(func, stream):
    while True:
        x = stream.next()
        if func(x):
            yield x

def integers_from(n):
    while True:
        yield n
        n += 1

def sieve():
    def divisible(x):
        return lambda e: e % x != 0
    stream = integers_from(2)
    while True:
        x = stream.next()
        yield x
        stream = stream_filter(divisible(x), stream)

def printn(n, stream):
    for _ in xrange(n):
        print stream.next(),
    print

def pi_summands():
    n, sign = 1, 1
    while True:
        yield 1.0/n*sign
        n += 1
        sign *= -1

def partial_sum(stream):
    acc = stream.next()
    yield acc
    while True:
        acc += stream.next()
        yield acc

