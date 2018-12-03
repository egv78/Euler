import math as m
import timeit
import os
import csv
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "p081_matrix.txt"

file_to_read = open(filename)

matrix = []

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    i = 0
    for row in csvReader:
        clean_row = list(filter(None, row))
        j = 0
        while j < len(clean_row) :
            clean_row[j] = int(clean_row[j])
            j+=1
        matrix.insert(i,clean_row)
        i += 1

matrix2 = [ [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331]
            ]

matrix3 = [ [0, 1, 2],
            [10, 11, 12],
            [20, 21, 22]
            ]

def make_triangular_matrix(square):
    size = len(square)
    triangle_size = 2*size - 1
    triangle_matrix = []
    triangle_i = 0
    max_square_i = size - 1
    
    while triangle_i < triangle_size:
        # print("Triangle i: ", str(triangle_i))
        new_triangle_row = []
        
        square_i = min(triangle_i, max_square_i)
        # print("Square i = ", str(square_i))
        
        if triangle_i > max_square_i:
            square_j = triangle_i - max_square_i
        else:
            square_j = 0
        # print("Square j = ", str(square_j))
        max_square_j = square_i
        
        end_square_i = triangle_i - max_square_i
        
        # print("End square i = ", str(end_square_i))
        
        while square_i >= end_square_i and square_j <= max_square_j:
            # print("i,j: ", str(square_i), ", ", str(square_j))
            new_triangle_row.append(square[square_i][square_j])
            square_j += 1
            square_i += -1
                
        triangle_matrix.append(new_triangle_row)
        triangle_i += 1
    return triangle_matrix

def collapse_triangle(triangle, break_point):
    working_row_num = len(triangle) - 2
    working_row = triangle[working_row_num]
    next_row_num = working_row_num + 1
    next_row = triangle[(next_row_num)]
    summed_row = []
    max_j = len(working_row) - 1
    j = 0
    
    if working_row_num < break_point:
        while j <= max_j:
            number1 = working_row[j]
            number2 = next_row[j]
            number3 = next_row[(j+1)]
            summed = min((number1+number2), (number1+number3))
            summed_row.append(summed)
            j += 1
    else:
        while j <= max_j:
            if j == 0:
                summed = working_row[j] + next_row[j]
                summed_row.append(summed)
            elif j == max_j:
                summed = working_row[j] + next_row[(j-1)]
                summed_row.append(summed)
            else:
                number1 = working_row[j]
                number2 = next_row[j-1]
                number3 = next_row[(j)]
                summed = min((number1+number2), (number1+number3))
                summed_row.append(summed)
            j += 1
    del(triangle[next_row_num])
    del(triangle[working_row_num])
    triangle.append(summed_row)
    if len(triangle) > 1:
        collapse_triangle(triangle, break_point)
    return triangle

triangle = make_triangular_matrix(matrix)
collapse_me = triangle.copy()

break_point = (m.floor(len(triangle)/2))

triangle_min_sum = collapse_triangle(collapse_me, break_point)

print("Smallest Sum is: ", str(triangle_min_sum))

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")
