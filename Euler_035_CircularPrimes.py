import math as m
import timeit

def rotate(l, n):
    rotated = l[n:] + l[:n]
    k = 1
    new_num_str = rotated[0]
    while k < len(rotated):
        new_num_str += rotated[k]
        k += 1
    
    return int(new_num_str)
    

start = timeit.default_timer()

low = 2
target = 1000000

Primes = []
Primes.append(2)
Primes.append(3)

i = 4
while i < target :
    next_value = i
    j = 0
    is_not_prime = 0
    new_target = m.floor(m.sqrt(next_value))
    if new_target == m.sqrt(next_value) :
        is_not_prime = 2
    
    while (is_not_prime < 2) and (Primes[j] <= new_target):
        is_not_prime = 1
        test_factor = Primes[j]
        if next_value % test_factor == 0:
            is_not_prime = 2 
            j = len(Primes)-1
        else :
            j += 1
        
    if is_not_prime == 1 :
        Primes.append(next_value)
   
    i += 1

circular = []

for number in Primes:
    digits = []
    ones = number % 10
    digits.append(str(ones))
    
    if number > 9:
        tens = number % 100 - ones
        tens_digit = tens / 10
        digits.append(str(int(tens_digit)))
    
    if number > 99:
        hundreds = number % 1000 - ones - tens
        hun_digit = hundreds / 100
        digits.append(str(int(hun_digit)))
        
    if number > 999:
        thousands = number % 10000 - ones - tens - hundreds
        thous_digit = thousands / 1000
        digits.append(str(int(thous_digit)))
    
    if number > 9999:
        tenthous = number % 100000 - ones - tens - hundreds - thousands
        ten_thou_digit = tenthous / 10000
        digits.append(str(int(ten_thou_digit)))
       
    if number > 99999:
        hunthous = number % 1000000 - ones - tens - hundreds - thousands - tenthous
        hun_thou_digit = hunthous / 100000
        digits.append(str(int(hun_thou_digit)))
        
    j = 0
    is_candidate = True
    # print(number)
    # print(digits)
    digits_in_order = digits[::-1]
    while j < len(digits) and is_candidate:
        rotation = rotate(digits_in_order, j)
        # print(rotation)
        if rotation in Primes:
            is_candidate = True
        else:
            is_candidate = False
        j += 1
     
    if is_candidate:
        circular.append(number)
        print("Candidate = ", int(number))
    

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")
print(str(len(circular)))
