import math as m
import timeit
start = timeit.default_timer()

naturals_summed = 0
squares_summed = 0

i = 1

while i < 101 :
    naturals_summed += i
    squares_summed += (i**2)
    i += 1

sum_squared = naturals_summed**2

difference = squares_summed - sum_squared

print "Sum of the squares", str(squares_summed)
print "Sum =", str(naturals_summed)
print "Square of the sum", str(sum_squared)

print "Difference =", difference

stop = timeit.default_timer()
time = stop - start
print "Runtime =",  time, "s"