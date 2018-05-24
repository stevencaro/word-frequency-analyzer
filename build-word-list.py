#!/usr/bin/python3

from collections import defaultdict
import re

word_list = {} #defaultdict(int)

# Because the word list contains nouns and prepositions, it is easier to
# process.  Nouns and prepositions are not conjugated as verbs are.
with open('top-500-words') as f:
    for line in f.readlines():
        line = line.strip()
        word_list[line] = 0

with open('top-100-verbs-with-conjugation') as f:
    for line in f.readlines():
        if line.startswith('#'):
            continue
        try:
            #(infinitive, present_progressive, past, present_perfect) = line.split()
            words = line.split()
            for word in words:
                word_list[word] = 0
        except:
            pass
            #print(' *', line, end='')

for key in sorted(word_list):
    print(key, word_list[key])
