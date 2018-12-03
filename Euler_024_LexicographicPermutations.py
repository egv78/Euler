import math as m
import timeit

start = timeit.default_timer()

target = 1000000  #max = 3628800
actual_target = target - 1

Numbers = [0,1,2,3,4,5,6,7,8,9]
Reversed = Numbers.copy()
Reversed.reverse()
Factorials = []
Remainders = []
Num_Factorials = []

remainder = actual_target
i = 0
while i < len(Reversed) :
    this_factorial= m.factorial(Reversed[i])
    number_this_factorial = m.floor(remainder / this_factorial)
    closest = this_factorial * number_this_factorial
    if closest > 0 :
        remainder = remainder % closest
       
    Factorials.append(this_factorial)
    Num_Factorials.append(number_this_factorial)
    Remainders.append(remainder)
    
    i += 1

built_number = []

Use_This = Numbers.copy()

while Num_Factorials[0] == 0 :
    Num_Factorials.pop(0)
    Use_This.pop(-1)

i = 0
while i < len(Num_Factorials) :
    new_digit = Use_This[(Num_Factorials[i])]
    Use_This.remove(new_digit)
    built_number.append(new_digit)
    
    i += 1
    

print(built_number)



stop = timeit.default_timer()
time = stop - start
print("Runtime =",  str('%.3f' %time), "s")