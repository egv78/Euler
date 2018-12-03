import math as m
import timeit
import bisect
start = timeit.default_timer()

class Number:
    def __init__(self, value) :
        self.value = int(value)
        if value == 0 :
            self.sum_divisors = 0
            self.divisors = [0]
            self.num_divisors = 0
            self.number_type = 4
        else :
            sum_divisors = 0
            next_factors = []
            
            root_value = m.floor(m.sqrt(value))
            if (root_value == m.sqrt(value)) :
                next_factors.append(root_value)
                divisor_stop = root_value
                sum_divisors += root_value
            else :
                divisor_stop = root_value + 1
            
            j = 1
            while j < divisor_stop :
                if ((value % j) == 0 ) :
                    high_factor = int(value / j)
                    next_factors.extend([j, high_factor])
                    sum_divisors += (j+high_factor)
                j += 1
            next_factors.remove(i)
            sum_divisors -= i
            next_num_div = len(next_factors)
            self.sum_divisors = sum_divisors
            self.divisors = next_factors
            self.num_divisors = next_num_div
            if (sum_divisors == 1) :  #prime
                number_type = 0
            elif (sum_divisors < i) : #deficient
                number_type = 1
            elif (sum_divisors == i) : # perfect
                number_type = 2
            elif (sum_divisors > i):  # abundant
                number_type = 3           
            else :
                number_type = 4      # other; really, should just be 0
            self.number_type = number_type
     

Numbers_List = []
Prime_List = []
Deficient_List = []
Perfect_List = []
Abundant_List = []
Abundants = []
Other_List = []

target = 28124  #  20162 #  5000 #  
i = 0
while i < target :
    new_number = Number(i)
    Numbers_List.insert(i,new_number)
    if   new_number.number_type == 0 :
        Prime_List.insert((len(Prime_List)), new_number)
    elif new_number.number_type == 1 :
        Deficient_List.insert((len(Deficient_List)), new_number)
    elif new_number.number_type == 2 :
        Perfect_List.insert((len(Perfect_List)), new_number)
    elif new_number.number_type == 3 :
        Abundant_List.insert((len(Abundant_List)), new_number)
        Abundants.append(new_number.value)
    elif new_number.number_type == 4 :
        Other_List.insert((len(Other_List)), new_number)
    
    i += 1

num_Primes = len(Prime_List)
num_Deficients = len(Deficient_List)
num_Perfects = len(Perfect_List)
num_Abundants = len(Abundant_List)
num_Others = len(Other_List)

print("There are", str(num_Primes), "Prime Numbers below ", str(target))
print("There are", str(num_Deficients), "Deficient Numbers (plus the Primes) below", str(target))
print("There are", str(num_Perfects), "Perfect Numbers below", str(target))
print("There are", str(num_Abundants), "Abundant Numbers below", str(target))

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  str('%.3f' % time), "s")

Two_Abundants = []
i = 0
while i < len(Abundants) :
    abundant_a = Abundants[i]
    j = i
    while j < len(Abundants) :
        abundant_b = Abundants[j]
        sum_two = abundant_a + abundant_b
        if sum_two < target: 
            Two_Abundants.append(sum_two)
        j += 1
    i += 1

stop_1 = timeit.default_timer()
time_1 = stop_1 - start
print("Runtime =",  str('%.3f' % time_1), "s")

Unique_Two = list(set(Two_Abundants))
Unique_Two.sort()
print(str(len(Unique_Two)))

sum_not_two = 0
Not_Two_Abundants = []
i = 0
while i < target :
    if (i in Unique_Two) :
        j = 1
    else :
        Not_Two_Abundants.append(i)
        sum_not_two += i
    i += 1

print("There are", str(len(Not_Two_Abundants)), "numbers below",  str(target), "that are NOT expressible as the sum of two abundant numbers.")
print("The sum of these numbers is", str(sum_not_two))

stop_2 = timeit.default_timer()
time_2 = stop_2 - start
print("Runtime =",  str('%.3f' % time_2), "s")