c, ans, day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 0, 1
for y in range(1901, 2001):
    for i in c:
        day += i
        if i == 28 and not(y % 4 or ((y % 100)and not(y % 400))):
            day += 1
        if day % 7 == 6:
            ans += 1
print(ans)
