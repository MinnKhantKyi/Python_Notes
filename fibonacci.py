import sys

def fib_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fib_generator(30)
print(sys.getsizeof(fib))
for i in fib:
    print(i)