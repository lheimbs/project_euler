import csv

with open('words.txt', 'r') as words:
    ws = csv.reader(words, delimiter=',', quotechar='"')
    words = []
    for row in ws:
        words += [word.lower() for word in row]

letters = {l: i+1 for i,l in enumerate('abcdefghijklmnopqrstuvwxyz')}
MAX = max([len(word) for word in words])
ns = {0.5*n*(1+n): n for n in range(1, MAX+1*26)}

n = 0
for word in words:
    value = 0
    for letter in word:
        value += letters[letter]
    if value in ns.keys():
        print(word)
        n += 1

print(n)

