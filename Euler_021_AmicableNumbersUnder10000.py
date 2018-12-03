import math as m
import timeit
start = timeit.default_timer()

# number, sum_of_divisors, divisors, number_divisors  ** proper divisors only **
number = 0
sum_of_divisors = 1
divisiors = 2
number_divisors = 3

Numbers = []
Numbers.insert(0,[0,0,[0],0])
Numbers.insert(1,[0,0,[0],0])
Numbers.insert(2,[2,1,[1],1])


target = 10000
i = 3
while i < target :
    Last_Number = Numbers[-1]
    next_value = i
    sum_divisors = 0
    next_factors = []
    
    root_value = m.floor(m.sqrt(next_value))
    if (root_value == m.sqrt(next_value)) :
        next_factors.append(root_value)
        divisor_stop = root_value
        sum_divisors += root_value
    else :
        divisor_stop = root_value + 1
    
    j = 1
    while j < divisor_stop :
        if ((next_value % j) == 0 ) :
            high_factor = int(next_value / j)
            next_factors.extend([j, high_factor])
            sum_divisors += (j+high_factor)
        j += 1
    next_factors.remove(i)
    sum_divisors -= i
    next_num_div = len(next_factors)
    
    Numbers.insert(next_value, [next_value, sum_divisors, next_factors, next_num_div])
        
    i += 1

Amicable_Numbers = []
sum_amicable_numbers = 0
i = 3

while i < len(Numbers) :
    candidate_a = i
    sum_a = Numbers[candidate_a][sum_of_divisors]
    while sum_a < target :
        candidate_b = sum_a
        sum_b = Numbers[candidate_b][sum_of_divisors]
        if ((sum_b == candidate_a) and not(sum_a == candidate_a) and not(candidate_b in Amicable_Numbers)) :
            next_pair_place = len(Amicable_Numbers)
            Amicable_Numbers.append(candidate_a)
            Amicable_Numbers.append(candidate_b)
            sum_amicable_numbers += (candidate_a + candidate_b)
        sum_a = target
    
    i += 1

print(Amicable_Numbers)
print(int(sum_amicable_numbers))



stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")