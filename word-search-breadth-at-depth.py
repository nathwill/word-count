#!/usr/bin/env python3

import sys
import math
import argparse

def get_words(word_file):
    return word_file.read().strip().split("\n")

def get_search_dict_at_depth(word_list = [], char_depth = 1):
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

def get_search_stats_at_depth(words, depth):
    search_dict = get_search_dict_at_depth(words, depth)
    counts = search_dict.values()

    stats = {}
    stats["avg"] = math.ceil(sum(counts)/len(counts))
    stats["worst_case"] = max(counts)

    return stats

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Count words at specified character depth')
    parser.add_argument('-f', '--filename', type=argparse.FileType('r'), required=True,
                     help='path to word dictionary (one word per line)', default='/usr/share/dict/words')
    parser.add_argument('-d', '--depths', metavar='D', type=int, nargs='+', required=True,
                     help='depth at which to measure word search breadth', default=3)
    args = parser.parse_args()
    
    w = get_words(args.filename)
    search_depth_breadth = {}

    for d in args.depths:
        search_depth_breadth[d] = get_search_stats_at_depth(w, d)

    print(search_depth_breadth)
