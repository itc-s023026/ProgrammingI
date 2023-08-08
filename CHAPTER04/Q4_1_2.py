def fib2(n):
    a, b = 0, 1
    while a < n:
        result = []
        print(a, end=" ")
        a, b = b, a + b
    return result


fib2(1000)
