candidate_numerators = []
candidate_denominators = []

reduced_numerators = []
reduced_denominators = []

a = 1
while a <= 9:
    b = 1
    while b <= 9:
        if b == 9:
            c = a + 1
            d = 1
        else:
            c = a
            d = b + 1
        while c <= 9:
            while d <= 9:
                numerator = 10*a + b
                denominator = 10*c + d
                fraction = numerator / float(denominator)
                #print(denominator)
                
                if a == c:
                    new_fraction = b / float(d)
                    if fraction == new_fraction:
                        candidate_numerators.append(numerator)
                        candidate_denominators.append(denominator)
                        reduced_numerators.append(b)
                        reduced_denominators.append(d)
                if a == d:
                    new_fraction = b / float(c)
                    if fraction == new_fraction:
                        candidate_numerators.append(numerator)
                        candidate_denominators.append(denominator)
                        reduced_numerators.append(b)
                        reduced_denominators.append(c)
                if b == c:
                    new_fraction = a / float(d)
                    if fraction == new_fraction:
                        candidate_numerators.append(numerator)
                        candidate_denominators.append(denominator)
                        reduced_numerators.append(a)
                        reduced_denominators.append(d)
                if b == d:
                    new_fraction = a / float(c)
                    if fraction == new_fraction:
                        candidate_numerators.append(numerator)
                        candidate_denominators.append(denominator)
                        reduced_numerators.append(a)
                        reduced_denominators.append(c)
                        
                
                d += 1
            d = 1
            c += 1
        b += 1
    a += 1

print(candidate_numerators)
print(candidate_denominators)
print(reduced_numerators)
print(reduced_denominators)

