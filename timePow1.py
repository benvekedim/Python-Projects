import time

t0 = time.time()

def power(x,y):

    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x,y // 2) * power(x,y // 2)

    return x * power(x,y // 2) * power(x,y // 2)

power(2,100)

t1 = time.time()

total = t1 - t0

print(total)