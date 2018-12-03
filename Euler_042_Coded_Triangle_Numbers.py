import math as m
import timeit
import os
start = timeit.default_timer()

path = 'c:\\Users\Eric\Projects\python1\Euler'
os.chdir(path)
filename = "p042_words.txt"

file = open(filename)
content = file.read()
no_quotes = content.replace('\"', '')
words = no_quotes.split(",")


def is_triangle(candidate):
    position = (-1+m.sqrt(1+8*candidate))/2
    if (position).is_integer():
        return 1
    else:
        return 0

def word_value(word):
    letter_positions = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
                    "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
                    "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
                    "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
                    }
    # word.strip('\"')
    word_sum = 0
    for letter in word:
        # print(letter)
        letter_value = letter_positions[letter]
        word_sum += letter_value
    return word_sum
    
triangle_words = 0

for word in words:
    # print(word)
    # triangle_words += is_triangle(word_value(word))
    value = word_value(word)
    triangle_words += is_triangle(value)

print("There are ", str(triangle_words), " triangle words in this doc.")

stop = timeit.default_timer()
time = stop - start
print("Runtime =",  time, "s")
