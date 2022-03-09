#Kullanım:

# import time
# t0 = time.time()
#code block
# t1 = time.time()
# total = t1 - t0

#saniyeye çevirmek için kullanılabilir
# second = total *(10 **(-6))
# print(total)

import time

t0 = time.time()

def power(x,y):
    return x ** y

power(2,1000)

t1 = time.time()

total = t1 - t0 #milisaniye

print(total)
