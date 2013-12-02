Y = lambda f:(lambda s:lambda x:f(s(s))(x))(lambda s:lambda x:f(s(s))(x))
Y1 = lambda f: (lambda x:x(x))((lambda s:lambda x:f(s(s))(x)))
Y2 = lambda f: (lambda x: x(x))(lambda y: f(lambda v: y(y)(v)))

def Y1(f):
    gen = lambda s:lambda x:f(s(s))(x)
    return gen(gen)
