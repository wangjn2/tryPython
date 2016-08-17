a = 1;

def outer(c):
    b = 1;
    def inner(d):
        print(a)
        print(b)
        print(c)
        print(d)
    return inner

