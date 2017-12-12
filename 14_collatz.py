import time
start_time = time.time()

num_steps = {2:1}
for n in range(3, 1000001):
    a, i = n, 0
    while True:
        a = a/2 if a % 2 == 0 else 3*a+1
        i += 1
        if a in num_steps:
            num_steps[n] = num_steps[a] + i
            break

print(max(num_steps, key=num_steps.get))
print("time elapsed: {:.2f}s".format(time.time() - start_time))
