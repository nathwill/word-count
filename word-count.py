#!/usr/bin/env python3

import sys
import math
import argparse

parser = argparse.ArgumentParser(description = 'Count words at specified character depth')
parser.add_argument('--filename', type=argparse.FileType('r'), required=True,
                     default='/usr/share/dict/words')
parser.add_argument('--depths', metavar='D', type=int, nargs='+', required=True,
                     help='char depth to traverse word list')
args = parser.parse_args()

# load word list from file
def get_words(word_file):
    return word_file.read().strip().split("\n")

# map word count for char depth
def get_word_dict_at_depth(word_list = [], char_depth = 1):
    word_dict = {}
    for word in word_list:
        if len(word) < char_depth:
            continue

        s = word[0:char_depth]
        if word_dict.get(s) == None:
            word_dict[s] = 1
        else:
            word_dict[s] += 1

    return word_dict

# compute avg word count at chart depth
w = get_words(args.filename)


depth_dict = {}
for d in args.depths:
    depth_dict[d] = get_word_dict_at_depth(w, d)
#print(depth_dict)

summary_dict = {}
for depth, char_count_map in depth_dict.items():
    counts = char_count_map.values()

    summary_dict[depth] = {}
    summary_dict[depth]["min"] = min(counts)
    summary_dict[depth]["avg"] = math.ceil(sum(counts)/len(counts))
    summary_dict[depth]["max"] = max(counts)
print(summary_dict)
