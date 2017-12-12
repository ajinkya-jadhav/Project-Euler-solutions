g = 0
i = 1
a = 1
d = 1
t = set()
while True:
    while i >= d :
        if i % d == 0:
            t.add(d)
            if len(t) > 500:
                print(i)
                g = 1
                break
        d += 1
    if g == 1:
        break
    a += 1
    i += a
    d = 1
    t = set()