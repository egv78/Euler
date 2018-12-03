import math as m
import timeit
import csv
import os
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "problem_18.csv"

Triangle = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        clean_row = list(filter(None, row))
        j = 0
        while j < len(clean_row) :
            clean_row[j] = int(clean_row[j])
            j+=1
        Triangle.insert(i,clean_row)
        i += 1

print(Triangle)


j = len(Triangle) - 1
print(Triangle[j])
while j > 0 :
    bottom_row = Triangle[j]
    new_row = Triangle[(j-1)]
    i = 0
    while i < len(new_row) :
        #new_row[i] = int(new_row[i]) + int(max(bottom_row[i], bottom_row[(i+1)]))
        new_row[i] += max(bottom_row[i], bottom_row[(i+1)])
        i += 1
    print(new_row)
    j -= 1


    

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")