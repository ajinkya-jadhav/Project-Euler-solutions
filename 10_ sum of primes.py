p = [3, 5]
n = 5
a = 0
while n < 2000000:
    for d in p:
        if n % d == 0:
            break
        a = d
    if a == p[len(p)-1]:
        p.append(n)
    if len(p) % 1000 == 0:
        print(len(p))
    n += 2
print(sum(p)+2)