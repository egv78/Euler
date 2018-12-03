import math as m
import timeit
start = timeit.default_timer()

# place, number of steps, sequence
Collatz = []
Collatz.insert(0,[0,0,[0]])
Collatz.insert(1,[1,1,[1]])

max_steps = 1
max_place = 1

i = 2
while i < 1000000 :
    Chain = []
    start_chain = i
    Chain.append(start_chain)
    next_step = int((start_chain / 2) if (start_chain % 2 == 0) else (3*start_chain + 1))
    while next_step > start_chain :
        Chain.append(next_step)
        next_step = int((next_step / 2) if (next_step % 2 == 0) else (3*next_step + 1))
    
    Chain.extend(Collatz[next_step][2])
    length_Chain = len(Chain)
    Collatz.insert(i,[i,length_Chain, Chain])
    max_place = start_chain if (length_Chain > max_steps) else max_place
    max_steps = length_Chain if (length_Chain > max_steps) else max_steps

    #print(Chain)
    
    i += 1

print("The longest sequence is", max_steps, ", which is for number", max_place)

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")