import math as m
import timeit
import csv
import os
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "problem_13.csv"

Grid = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        Grid.insert(i,int(row[0]))
        i += 1

sum_numbers = 0
for item in Grid :
    sum_numbers += item
    
size = m.floor(m.log10(sum_numbers))

print("size = 10^"+str(size))

first_ten = sum_numbers // 10**(size-9)

print(str(first_ten))

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")