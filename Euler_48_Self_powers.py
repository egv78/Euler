import math as m
import timeit

start = timeit.default_timer()

digits = 10

# trunc_sum = 0
sum_num = 0

i = 1

while i <= 1000:
    new_num = i ** i
    sum_num += new_num
        
    i += 1

trunc_sum = sum_num % (10**digits)

print("The last ten digits are ", str(trunc_sum), ".")

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")
