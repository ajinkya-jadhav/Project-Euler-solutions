l = a = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        b = i*j
        a = str(b)
        if a == a[::-1] and b > l:
            l = b
print(l)
