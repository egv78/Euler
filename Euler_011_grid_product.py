import math as m
import timeit
import csv
import os
start = timeit.default_timer()

def check_by_rows(Grid, top_product, span) :
    # check horizontal
    for row in Grid :
        columns = len(row)
        i = 0
        while (i < (columns - span)) :
            product_candidate = 1
            j = i
            while j < (i+span +1) :
                product_candidate *= int(row[j])
                j += 1
            if (product_candidate > top_product) :
                top_product = product_candidate
            i +=1
    return(top_product)

def check_diagonals(Grid, top_product, span) :
    rows = len(Grid)
    cols = len(Grid[0])
    i = 0
    while (i < (rows - span)) :
        #product_candidate = 1
        j = 0
        while (j < (cols - span)) :
            product_candidate = 1
            k = 0
            while (k < (span + 1)) :
                r = i + k
                c = j + k
                product_candidate *= int(Grid[r][c])
                k += 1
            if (product_candidate > top_product) :
                top_product = product_candidate
            j += 1
        i += 1
    return(top_product)


path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "problem_11.csv"

Grid = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        Grid.insert(i,row)
        i += 1

top_product = 1
span = 3

top_product = check_by_rows(Grid, top_product, span)
Transposed = [*zip(*Grid)]

top_product = check_by_rows(Transposed, top_product, span)
top_product = check_diagonals(Grid, top_product, span)
Reversed = Grid[::-1]

top_product = check_diagonals(Reversed, top_product, span)

print(top_product)

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")