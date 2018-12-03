import timeit
start = timeit.default_timer()

class number():
    def __init__(self, value, name, name_length) :
        self.value = value
        self.name = name
        self.name_length = name_length

def give_name (value) :
    defining_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 
                    20, 30, 40, 50, 60, 70, 80, 90, 
                    1000, 100, ]
    named_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 
                    20, 30, 40, 50, 60, 70, 80, 90, 1000]
                    
    defining_name = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", 
                "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                "onethousand", "hundred"]
    
    if value in named_values :
        name = defining_name[named_values.index(value)]
    elif value < 100 :
        tens = (value // 10)*10
        tens_name = defining_name[named_values.index(tens)]
        ones = value % 10
        ones_name = defining_name[named_values.index(ones)]
        name = tens_name+ones_name
    elif (value % 100 == 0):
        hundreds = value // 100
        hundreds_name = defining_name[named_values.index(hundreds)]
        hundreds_name += "hundred"
        name = hundreds_name
    else :
        hundreds = value // 100
        hundreds_remainder = value % (hundreds * 100)
        hundreds_name = defining_name[named_values.index(hundreds)]
        hundreds_name += "hundredand"
        if (hundreds_remainder) in named_values :
            name_and = defining_name[named_values.index((hundreds_remainder))]
            name = hundreds_name + name_and
        else :
            tens = (hundreds_remainder // 10) * 10
            tens_name = defining_name[named_values.index(tens)]
            ones = hundreds_remainder % (tens)
            ones_name = defining_name[named_values.index(ones)]
            name = hundreds_name+tens_name+ones_name
    
    return name

Numbers = []
total_length = 0

i = 0
while i < 1000 :
    value = i + 1
    name = give_name(value)
    length = len(name)
    total_length += length
    Numbers.append(number(value, name, length))
    #print str(value), name, length
    i += 1

print "The total letters in the names of numbers 1-1000 =", str(total_length)

stop = timeit.default_timer()
time = stop - start
print "Runtime =",  time, "s"