# ----------------------------------------
# Program:   Chapter 20 Exercise 3
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      07/05/2026
# ----------------------------------------
alice_file = open("alice.txt", "r", encoding="utf-8") #open the file with story, read it. 
text = alice_file.read()                              #(had to add utf 8 wouldnt open my file)
alice_file.close()

text = text.lower()                # converts all letters to lower case

for ch in ",.!?;:\"()[]_*-":       # changes all punctuation to spaces
    text = text.replace(ch, " ") 

words = text.split()               # splits all text into words

word_counts = {}                   # creates word storage 

for each_word in word              # counts how many times each word appears in text
    word_counts[each_word] = word_counts.get(each_word, 0) + 1

word_list = list(word_counts.items()) # put words into list and sorts a-z
word_list.sort()

output_file = open("alice_words.txt", "w") # create output file

output_file.write("Word              Count\n") # headings on list / output file
output_file.write("=======================\n")

for word, count in word_list:
    output_file.write(word + " " * (18 - len(word)) + str(count) + "\n")

output_file.close()

print("Done")
print("alice occurs", word_counts.get("alice", 0), "times")
