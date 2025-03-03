#Code to Reverse words in a sentence.
# Input string
s = "Geeks or nerds"

# Split the string into words, reverse the list of words, and join them back
reversed_words = ' '.join(s.split()[::-1])

print(reversed_words)
