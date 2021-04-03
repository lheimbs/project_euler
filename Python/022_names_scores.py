import numpy as np

names = []
with open('names.txt', 'r') as names_file:
    names = names_file.read().split(',')

names = sorted([name.replace('"', '').lower() for name in names])
letter_scores = {
    letter: i+1 for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz')
}

names = {
    name: (i+1) * sum([letter_scores[letter] for letter in name])
        for i, name in enumerate(names)
}
print(sum(names.values()))

