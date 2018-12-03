import math as m
import timeit
import os
import csv
from itertools import permutations 
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "Primes2to10000000.csv"

file_to_read = open(filename)

matrix = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        clean_row = list(filter(None, row))
        for item in clean_row:
            matrix.append(int(item))
        if (i % 1000) == 0:
            print("Row ", str(i))
        # j = 0
        # while j < len(clean_row) :
        #     clean_row[j] = int(clean_row[j])
        #     j+=1
        # matrix.insert(i,clean_row)
        i += 1

print("matrix read")
pan7 = []

for p in permutations(range(1, 8)):
    new_num = 0
    len_num = len(p)
    i = 0
    while i < len_num:
        new_num += p[i]*(10**(len_num-1-i))
        i += 1
    pan7.append(new_num)

pan7.sort(reverse=True)

candidate = 0
j = 0

while candidate == 0 and j < len(pan7):
    number = pan7[j]
    if number in matrix:
        print("We're done here.  The number is ", str(number))
        candidate = number
    j += 1
if candidate == 0:
    print("No seven digit pandigital primes.")


if candidate < 2:
    pan4 = []
    
    for p in permutations(range(1, 5)):
        new_num = 0
        len_num = len(p)
        i = 0
        while i < len_num:
            new_num += p[i]*(10**(len_num-1-i))
            i += 1
        pan4.append(new_num)
    
    pan4.sort(reverse=True)
    
    candidate = 0
    j = 0
    
    while candidate == 0 and j < len(pan4):
        number = pan4[j]
        if number in matrix:
            print("We're done here.  The number is ", str(number))
            candidate = number
        j += 1
    if candidate == 0 :
        print("I done messed up.")

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")
