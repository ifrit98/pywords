#!/usr/bin/python3

from itertools import permutations
from pprint import pprint
import numpy as np
import csv
from sys import maxsize
import os

np.set_printoptions(threshold=maxsize)


# TODO: Add wildcard functionality (blank tiles)
LETTERS = list('abcdefghijklmnopqrstuvwxyz')



def letter_ws(dir='word-lists'):
    csvs = os.listdir(dir)
    wset = set()
    for fn in csvs:
        path = os.path.join(os.path.abspath(dir), fn)
        with open(path, newline='\n') as f:
            reader = csv.reader(f, delimiter='\n')
            try:
                for w in reader:
                    if not w: continue
                    if len(w[0]) > 1 and len(w[0]) < 9 and '-' not in w[0]:
                        wset.add(w[0][:-1] if w[0][-1] == ' ' else w[0])
            except UnicodeDecodeError:
                print("unicode error")
                break

    return wset


def get_wordset(fp=None):
    if not fp:
        fp = 'words.txt'

    wset = set()
    with open(fp, newline='\n') as f:
        reader = csv.reader(f, delimiter='\n')
        for w in reader:
            if len(w[0]) > 1 and len(w[0]) < 9 and '-' not in w[0]:
                wset.add(w[0])
    return wset.union(letter_ws())


def permchr(iterchr, i=None):
    if not i:
        i = len(iterchr)
    p = list(permutations(iterchr, i))
    p = list(map(lambda x: ''.join(x).lower(), p))
    return np.asarray(p)

def gen_matches(letters):
    matches = list()
    for i in range(1, len(letters)):
        p = permchr(letters, i+1)
        idx = np.asarray(list(map(lambda x: x in ws, p)))
        potential_matches = p[idx]
        if len(potential_matches):
            matches.append(potential_matches)
    return np.concatenate(matches) if len(matches) else []



if __name__ == "__main__":
    ws = get_wordset()
    while (True):
        inp = input("Enter letters:\n")
        if inp in ["q"]:
            print("Exiting...")
            exit(0)
        if not inp.isalnum():
            print("Please enter a valid string (or 'q' to quit)...")
            continue
        letters = list(inp)
        matches = gen_matches(letters)
        pprint(matches)
