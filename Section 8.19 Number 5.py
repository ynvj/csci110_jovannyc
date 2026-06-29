# ----------------------------------------
# Program:   Chapter 8 Exercise 5
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      06/27/2026
# ----------------------------------------

text = """
Dumped wet and momentary on a dull ground
that's been clear but clearly sleeping, for days.
Last snow melts as it falls, piles up slush, runs in first light
making a music in the streets we wish we could keep.
Last snow. That's what we'll think for weeks to come.
Close sun sets up a glare that smarts like a good cry.
We could head north and north and never let this season go.
Stubborn beast, the body reads the past in the change of light,
knows the blow of grief in the time of trees' tight-fisted leaves.
Stubborn calendar of bone. Last snow. Now it must always be so.
"""

text = text.replace(".", "") # punctuation removal 
text = text.replace(",", "") # punctuation removal
text = text.replace("'", "") # punctuation removal 
text = text.replace("-", "") # punctuation removal

words = text.split() # breaks apart the text into list of words

total_num_of_words = len(words) # count the total number o words

words_with_e = 0 # count the words that have an e

for each_word in words:
    if "e" in each_word:
        words_with_e = words_with_e + 1

percent = (words_with_e / total_num_of_words) * 100 # percentage calculations

print("Your text contains", total_num_of_words, "words, of which", words_with_e, # result
      "(" + str(round(percent, 1)) + "%)", "contain an 'e'.")
