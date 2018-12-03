candidate_numerators = []
candidate_denominators = []

a = 4
b = 9
c = 9
d = 8

numerator = 10*a + b
denominator = 10*c + d
fraction = numerator / float(denominator)

if a == c:
    new_fraction = b / float(d)
    if fraction == new_fraction:
        candidate_numerators.append(numerator)
        candidate_denominators.append(denominator)
if a == d:
    new_fraction = b / float(c)
    if fraction == new_fraction:
        candidate_numerators.append(numerator)
        candidate_denominators.append(denominator)
if b == c:
    new_fraction = a / float(d)
    if fraction == new_fraction:
        candidate_numerators.append(numerator)
        candidate_denominators.append(denominator)
if b == d:
    new_fraction = a / float(c)
    if fraction == new_fraction:
        candidate_numerators.append(numerator)
        candidate_denominators.append(denominator)

print(candidate_numerators)
print(candidate_denominators)