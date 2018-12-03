import math as m
import timeit
start = timeit.default_timer()

def find_next_prime(Primes) :
    number_of_primes = len(Primes)
    Prime_candidate = Primes[(number_of_primes-1)] + (1.0 if number_of_primes == 1 else 2)
    i = 0
    while (i < len(Primes)) :
        if (Prime_candidate % Primes[i] == 0) :
            Prime_candidate += 1.0
            i = 0
        else :
            i += 1
    return (Prime_candidate) 

Primes = [2.0]

while len(Primes) < 10001 :
    next_prime = find_next_prime(Primes)
    Primes.append(next_prime)

print "The 10,001st prime number is", Primes[-1]


stop = timeit.default_timer()
time = stop - start
print "Runtime =",  time, "s"