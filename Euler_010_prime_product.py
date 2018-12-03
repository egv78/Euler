import math as m
import timeit
start = timeit.default_timer()

def find_next_prime(Primes) :
    number_of_primes = len(Primes)
    Prime_candidate = Primes[(number_of_primes-1)] + (1 if number_of_primes == 1 else 2)
    i = 0
    while (i < len(Primes)) :
        root_candidate = m.ceil(m.sqrt(Prime_candidate))
        if (Prime_candidate % Primes[i] == 0) :
            Prime_candidate += 2
            i = 0
        elif (Primes[i] > root_candidate) :
            i = len(Primes)
        else :
            i += 1
    return (Prime_candidate) 

Primes = [2, 3]

while Primes[-1] < 2000000 :
    next_prime = find_next_prime(Primes)
    Primes.append(next_prime)

number_of_primes = len(Primes)
last = number_of_primes - 1

print("The prime in place", last,"is", Primes[-2])


sum_primes = 0

i = 0
while (i < (len(Primes)-1)) :
    sum_primes += Primes[i]
    i += 1

print("The sum of these primes is: ", sum_primes)

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")