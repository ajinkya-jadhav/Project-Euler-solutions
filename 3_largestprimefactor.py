m = 600851475143
for a in range(3, int(m/2)+1, 2):
    if not (m % a):
        m = m/a
    if m == 1:
        print(a)
        break
