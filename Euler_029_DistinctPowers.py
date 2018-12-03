value = 100
a_max = value
b_max = value

powers_list = []

a = 2
b = 2

while a <= a_max:
    while b <= b_max:
        new_number = a**b
        powers_list.append(new_number)
        b += 1
    b = 2
    a += 1

unique_list = set(powers_list)
distinct_terms = len(unique_list)

print("a = ", a)
print("b = ", b)
print("distinct terms", distinct_terms)
