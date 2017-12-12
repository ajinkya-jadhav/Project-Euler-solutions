def fib_ix(n):                 # Returns index
    a, b, i  = 1, 1, 0
    while a <= n:
        a, b = b, a+b
        i += 1
    return i
def fib(ix):
    a, b, c = 1, 2, 2
    while c <= ix:
        a, b, = b, a+b
        c += 1
    return a
l = fib_ix(4000000)
ans = 0
for j in range(2, l, 3):
    ans += fib(j)
print(ans)