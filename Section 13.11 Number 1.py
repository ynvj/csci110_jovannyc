# ----------------------------------------
# Program:   Chapter 13 Exercise 1
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      07/05/2026
# ----------------------------------------
old_file = open("old_file.txt", "r") # the original file opened and analyzed
lines = old_file.readlines() # lines from original file stored
old_file.close()

lines.reverse()

new_file = open("new_file.txt", "w") # new file created

for each_line in lines:
    new_file.write(each_line)

new_file.close()
print("Done")
