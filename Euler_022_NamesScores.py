import math as m
import timeit
import csv
import os
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "problem_22.csv"

Names = []
firstname = "-"
Names.insert(0,firstname)

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        name_to_add = str(row)
        name_to_add.replace("[", "")
        name_to_add.replace("]", "")
        name_to_add.replace("'", "")
        Names.extend(row)
        i += 1

Sorted_Names = sorted(Names)

Letters = ["-", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

number_Names = len(Sorted_Names)

names_score = 0
i = 1
while i < number_Names :
    j = 0
    name_value = 0
    this_name = Sorted_Names[i]
    name_length = len(this_name) 
    letter_scores = 0
    while j < name_length :
        letter_value = Letters.index(this_name[j])
        letter_scores += letter_value
        j += 1
    name_value = letter_scores * i
    names_score += name_value
    
    
    i += 1


stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")