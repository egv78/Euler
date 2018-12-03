import math as m
import timeit
start = timeit.default_timer()

big_number = 2**1000

big_num_str = str(big_number)

num_digits = len(big_num_str)

sum_digits =0
i = 0

while i < num_digits :
    sum_digits += int(big_num_str[i])
    i += 1

print("Big number is", big_number, "; it has", num_digits," digits which sum to:", sum_digits)

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")