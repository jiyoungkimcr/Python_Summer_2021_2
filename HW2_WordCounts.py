'''
Please write a program that reads a text file containing some text and for each word in the file counts how many times it
appears. Please note you can use a dictionary structure. Before starting to count words it might be necessary to delete
all punctuation and special symbols (new line, tab etc.) and put all words in lower case.
Code writer: Jiyoung Kim
'''

import string

# Open text file in read mode
# Remove all punctuation, special symbols, lower/upper case difference

my_file = 'Obama_WordsMatter.txt'
with open(my_file, 'r') as f:
    for line in f:
        line = line.lower()
        line = line.strip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        words = line.split(" ")
        counts = dict()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

for k,v in counts.items():
    print(k, ":", v)
