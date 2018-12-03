size = 1001
target = size**2
sum = 0

number = 1
sum += number
increment = 0

while number < target:
    increment += 2
    iteration = 1
    while iteration <=4:
        number += increment
        sum += number
        iteration += 1


print("number = ")
print (number)
print("sum = ")
print(sum)