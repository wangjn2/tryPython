#!/usr/bin/env python3
a = 1;

def outer(c):
    b = 2;
    def inner(d):
        print("a: %s" % a)
        print("b: %s" % b)
        print("c: %s" % c)
        print("d: %s" % d)
    return inner

b = 1

f1 = outer(3)
f1(4)

