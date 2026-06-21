# ----------------------------------------
# Program:   Chapter 7 Exercise 9
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      06/20/2026
# ----------------------------------------

def print_triangular_numbers(n):
    total = 0                   # sets "starting point"

    for i in range(1, n + 1):   # "+1" to cover full range 
        total = total + i
        print(i, total)         # prints triangle numbers
