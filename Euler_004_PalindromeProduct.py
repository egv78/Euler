import timeit
start = timeit.default_timer()

Products = []
Palindrome_Products = []

i = 999
while i > 800 :
    j = i
    while j > 99 :
        product = i * j
        Products.append(product)
        product_as_str = str(product)
        if len(product_as_str) == 6 :
            if ((product_as_str[0] == product_as_str[5]) and (product_as_str[1] == product_as_str[4]) and (product_as_str[2] == product_as_str[3])) : 
                if not (product in Palindrome_Products) :
                    Palindrome_Products.append(product)
        else :
            if ((product_as_str[0] == product_as_str[4]) and (product_as_str[1] == product_as_str[3])) : 
                if not (product in Palindrome_Products) :
                    Palindrome_Products.append(product)
        j -= 1
    i -= 1

# remove duplicates
Unique_Palindromes = []

i = 0
while i < len(Palindrome_Products) :
    if not (Palindrome_Products[i] in Unique_Palindromes) :
        Unique_Palindromes.append(Palindrome_Products[i])
    i +=1

Unique_Palindromes.sort()

print (Unique_Palindromes[-1])


        
 
stop = timeit.default_timer()
time = stop - start
print "Runtime =",  time, "s"