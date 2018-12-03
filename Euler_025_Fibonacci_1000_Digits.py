import math as m
import timeit

start = timeit.default_timer()

target = 1000  #max = ?

Fibonacci = []
Fibonacci.append(0)
Fibonacci.append(1)

i = 1
digits = 1 + m.floor(m.log10(Fibonacci[i]))

while digits < target :
    i += 1
    new_fib = Fibonacci[(i-1)] + Fibonacci[(i-2)]
    Fibonacci.append(new_fib)
    digits = 1 + m.floor(m.log10(Fibonacci[i]))

place = len(Fibonacci)-1

print("The Fibonacci number with index number", str(place), "is the first with", str(target), "digits.")

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  str('%.3f' %time), "s")