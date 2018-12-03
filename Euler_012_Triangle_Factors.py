import math as m
import timeit
start = timeit.default_timer()

# place, number, divisors, number_divisors
Triangle_Numbers = []
Triangle_Numbers.insert(0,[1,1,[1],1])

target = Triangle_Numbers[-1][3]
while target <= 500 :
    Last_Triangle = Triangle_Numbers[-1]
    next_place = Last_Triangle[0]+1
    next_value = Last_Triangle[1] + next_place
    next_factors = []
    
    root_value = m.floor(m.sqrt(next_value))
    if (root_value == m.sqrt(next_value)) :
        next_factors.append(root_value)
        divisor_stop = root_value
    else :
        divisor_stop = root_value + 1
    
    i = 1
    while i < divisor_stop :
        if ((next_value % i) == 0 ) :
            high_factor = int(next_value / i)
            next_factors.extend([i, high_factor])
        i += 1
    next_num_div = len(next_factors)
    
    Triangle_Numbers.insert(next_place, [next_place, next_value, next_factors, next_num_div])
        
    target = Triangle_Numbers[-1][3]
    
#print("Divisors:", target)

#for row in Triangle_Numbers :
#    print(row)

print(Triangle_Numbers[-1])

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")