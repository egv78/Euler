i = 1
Fibonacci = [1,1]
total = 0

while (Fibonacci[i] < 4000000) :
    i += 1
    newnum = (Fibonacci[i-1]+Fibonacci[i-2])
    Fibonacci.append(newnum)
    if ((Fibonacci[i] % 2) == 0) :
        total += Fibonacci[i]

print(total)