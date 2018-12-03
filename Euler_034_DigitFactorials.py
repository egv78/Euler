import math

target = 2200000  # 360000

candidates = []
sum_candidates = 0

i = 3

while i < target:
    number = i
    ones = number % 10
    ones_fact = math.factorial(ones)
    digits_to_fact = ones_fact
    
    if i > 9:
        tens = number % 100 - ones
        tens_digit = tens / 10
        tens_fact = math.factorial(tens_digit)
        digits_to_fact += tens_fact
    
    if i > 99:
        hundreds = number % 1000 - ones - tens
        hun_digit = hundreds / 100
        hun_fact = math.factorial(hun_digit)
        digits_to_fact += hun_fact
    
    if i > 999:
        thousands = number % 10000 - ones - tens - hundreds
        thous_digit = thousands / 1000
        thous_fact = math.factorial(thous_digit)
        digits_to_fact += thous_fact
    
    if i > 9999:
        tenthous = number % 100000 - ones - tens - hundreds - thousands
        ten_thou_digit = tenthous / 10000
        ten_thou_fact = math.factorial(ten_thou_digit)
        digits_to_fact += ten_thou_fact
    
    if i > 99999:
        hunthous = number % 1000000 - ones - tens - hundreds - thousands - tenthous
        hun_thou_digit = hunthous / 100000
        hun_thou_fact = math.factorial(hun_thou_digit)
        digits_to_fact += hun_thou_fact
    
    if i > 999999:
        millions = number - ones - tens - hundreds - thousands - tenthous - hunthous
        mill_digit = millions / 1000000
        mill_fact = math.factorial(mill_digit)
        digits_to_fact += mill_fact
        
    if number == digits_to_fact:
        candidates.append(number)
        sum_candidates += number
    
    i += 1

print(candidates)
print(sum_candidates)
