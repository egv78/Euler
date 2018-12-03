import math as m
import timeit
start = timeit.default_timer()

max_value = 1000

a_max = 1000 // 3

a = 1
while (a < a_max) :
    b_max = (max_value - a) // 2
    b = 1
    while (b < b_max) :
        c = (1000 - a - b)
        if ((a**2 + b**2) == (c**2)) :
            print("a=",a,"b=",b,"c=",c)
            product = a*b*c
            print("The product is:", product)
            a = a_max+1
        else :
            c += 1
        b += 1
    a += 1
        
        
        
stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")