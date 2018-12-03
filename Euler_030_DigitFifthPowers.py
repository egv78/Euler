target = 1000000  # 360000
power = 5

candidates = []
sum = 0

i = 2

while i < target:
    number = i
    ones = number % 10
    tens = number % 100 - ones
    hundreds = number % 1000 - ones - tens
    thousands = number % 10000 - ones - tens - hundreds
    tenthous = number % 100000 - ones - tens - hundreds - thousands
    hunthous = number - ones - tens - hundreds - thousands - tenthous
        
    tens_digit = tens / 10
    hun_digit = hundreds / 100
    thous_digit = thousands / 1000
    ten_thou_digit = tenthous / 10000
    hun_thou_digit = hunthous / 100000
    
    digits_to_power = ones**power + tens_digit**power + hun_digit**power + thous_digit**power + ten_thou_digit**power + hun_thou_digit**power
    
    if number == digits_to_power:
        candidates.append(number)
        sum += number
    
    i += 1

print(candidates)
print(sum)
