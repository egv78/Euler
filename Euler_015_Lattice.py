import math as m
import timeit
start = timeit.default_timer()

Pascal = []
Pascal.insert(0, [0])
Pascal.insert(1, [1])

target = 41

level = 2

while level <= target :
    previous = level - 1
    old_row = Pascal[previous]
    length_previous = len(old_row)
    i = 1
    new_row = []
    new_row.append(1)
    while i < previous :
        new_row.append((old_row[i] + old_row[(i-1)]))
        i += 1
    new_row.append(1)
    print(max(new_row))
    Pascal.insert(level,new_row)
    level +=1

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")