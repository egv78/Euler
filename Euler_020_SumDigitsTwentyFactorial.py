import math as m
import timeit
start = timeit.default_timer()

big_number = m.factorial(100)

big_num_str = str(big_number)
length_number = len(big_num_str)

sum_digits = 0
i = 0

while i < length_number :
    sum_digits += int(big_num_str[i])
    i += 1

print("100! =", str(big_number))
print("It has", str(length_number), "digits, which sum to: ", str(sum_digits))


stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")