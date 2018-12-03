import math as m
import timeit
import csv
import os
start = timeit.default_timer()

low = 2
target = 10000000

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

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "Primes"+str(low)+"to"+str(target)+".csv"

with open(filename, "w+", newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    new_row = []
    i = 0
    num_primes = len(Primes)
    while i < num_primes :
        add = (i+50) if (i < (num_primes - 49)) else num_primes
        new_row = Primes[i:add]
        filewriter.writerow(new_row)
        i += 50

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")