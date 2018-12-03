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

target = 600851475143.0
#target = 2484
root_target = m.ceil(m.sqrt(target))

#building a list of primes
Primes = [2.0]

Low_Factors = []
High_Factors = []
if ((target % 2.0) == 0) :
    Low_Factors.append(2.0)
    High_Factors.append((target / 2.0))

current_max = target // Primes[-1]

while Primes[-1] < root_target :
    next_prime = find_next_prime(Primes)
    Primes.append(next_prime)
    if ((target % Primes[-1]) == 0) :
        Low_Factors.append(next_prime)
        High_Factors.append((target / next_prime))

High_Primes = []

High_Factors = High_Factors[::-1]

i = 0
while (i < len(High_Factors)) :
    j = 0
    candidate_factor = High_Factors[i]
    while (j < len(Low_Factors)) :
        while ((candidate_factor % Low_Factors[j]) == 0 ) :
            candidate_factor = (candidate_factor / Low_Factors[j])
        j += 1
    if (candidate_factor not in High_Primes and candidate_factor > 1):
        High_Primes.append(candidate_factor)
    i +=1

print "# of all primes below root target =", str(len(Primes))
print "# of prime factors below root target =", str(len(Low_Factors))
print(Low_Factors)
print "# of factors ABOVE root target =", str(len(High_Factors))
print(High_Factors)
print "# of prime factors ABOVE root target =", str(len(High_Primes))
print(High_Primes)


Prime_Factors = Low_Factors
Prime_Factors.extend(High_Primes)

print "Total prime factors =", str(len(Prime_Factors))
print(Prime_Factors)

stop = timeit.default_timer()
time = stop - start
print "Runtime =",  time, "s"