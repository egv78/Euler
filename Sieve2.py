import math as m
import timeit
import csv
import os
start = timeit.default_timer()

starting_low = 100000000
increments = 10000000
number_iterations = 10

final_target = starting_low*number_iterations
root_target = m.floor(m.sqrt(final_target))

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "Primes2to1000000.csv"
Primes = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if int(row[0]) < root_target:
            i = 0
            while i < len(row):
                Primes.append(int(row[i]))
                i += 1

pass_through = 0
while pass_through < number_iterations:
    low = starting_low * pass_through if pass_through > 0 else 2
    target = low + starting_low if pass_through > 0 else starting_low
    
    New_Primes = []
    
    i = low
    while i < target:
        next_value = i
        j = 0
        is_not_prime = 0
        new_target = m.floor(m.sqrt(next_value))
        if new_target == m.sqrt(next_value):
            is_not_prime = 2
        
        while (is_not_prime < 2) and (j < len(Primes)) and (Primes[j] <= new_target):
            is_not_prime = 1
            test_factor = Primes[j]
            if next_value % test_factor == 0:
                is_not_prime = 2 
                j = len(Primes)-1
            else :
                j += 1
            
        if is_not_prime == 1:
            New_Primes.append(next_value)
    
        i +=1
    
    path = 'c:\\Users\Eric\Projects\python1\Euler'
    os.chdir(path)
    filename = "Primes"+str(low)+"to"+str(target)+".csv"
    
    with open(filename, "w+", newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        new_row = []
        i = 0
        num_primes = len(New_Primes)
        while i < num_primes:
            add = (i+50) if (i < (num_primes - 49)) else num_primes
            new_row = New_Primes[i:add]
            filewriter.writerow(new_row)
            i += 50
    
    stop_now = timeit.default_timer()
    time_now = stop_now - start
    print("Runtime in pass through", str(int(pass_through)), "is",  str('%.3f' % time_now), "s")
    
    pass_through += 1

stop = timeit.default_timer()
time = stop - start
print("Runtime in pass through", str(int(pass_through)), "is",  str('%.3f' % time), "s")