# ----------------------------------------
# Program:   Chapter 11 Exercise 10
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      06/28/2026
# ----------------------------------------

def replace(s, old, new):
    pieces = s.split(old) # splits the string into different pieces
    new_string = new.join(pieces) # join the different pieces  
    return new_string # updated string

print(replace("Mississippi", "i", "I"))

s = "I love spom! Spom is my favorite food. Spom, spom, yum!" # the orignal string

print(replace(s, "o", "a"))
print(replace(s, "om", "am"))

