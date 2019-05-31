#!/usr/bin/env python3
###############################################################################
# Word combination generator. Run with python3. 
#
# Author: PotatoMaster101
# Date:   31/05/2019
###############################################################################

import argparse
import string
import sys
from datetime import datetime

def get_args():
    """
    Returns the user arguments. 
    """
    p = argparse.ArgumentParser(description="Word combination generator.")
    p.add_argument("input", type=str, help="string to generate combinations")
    p.add_argument("-p", "--pool", type=str, default="", dest="pool", 
            help="pool of characters that can be substituted")
    p.add_argument("-pA", "--pool-alph", action="store_true", dest="palph", 
            help="include all alphabetical characters in the pool")
    p.add_argument("-pN", "--pool-num", action="store_true", dest="pnum", 
            help="include all numerical characters in the pool")
    p.add_argument("-pL", "--pool-low", action="store_true", dest="plow", 
            help="include all lowercase characters in the pool")
    p.add_argument("-pU", "--pool-up", action="store_true", dest="pup", 
            help="include all uppercase characters in the pool")
    p.add_argument("-pP", "--pool-punc", action="store_true", dest="ppunc", 
            help="include all punctuation characters in the pool")
    p.add_argument("-s", "--sub-char", type=str, default="?", dest="subchar", 
            help="character that will be substituted")
    p.add_argument("-v", "--verbose", action="store_true", dest="verb", 
            help="produce verbose output")
    p.add_argument("-o", "--output", type=str, default=None, dest="out", 
            help="output file name")
    return p


def get_pool(argp):
    """
    Returns a pool of characters specified by the user. 
    """
    pool = argp.pool
    if argp.palph:
        pool += string.ascii_letters
    if argp.pnum:
        pool += string.digits
    if argp.plow:
        pool += string.ascii_lowercase
    if argp.pup:
        pool += string.ascii_uppercase
    if argp.ppunc:
        pool += string.punctuation
    if not pool:
        pool += string.ascii_letters + string.digits + string.punctuation
    return "".join(set(pool))


def get_subindex(string, ch):
    """
    Finds all indexes of the specified character in the string. 
    """
    return [c for (c, i) in enumerate(string) if i == ch]


def increment_idx(poolidx, maxidx):
    """
    Increments the pool indexes. 
    """
    if not poolidx:
        return False

    poolidx[0] += 1
    if poolidx[0] <= maxidx:        # no need to update others
        return poolidx

    updated = False
    i = 1
    while (i < len(poolidx)) and (not updated):     # update others
        if poolidx[i] < maxidx:
            poolidx[i] += 1
            poolidx[0:i] = [0] * i
            updated = True
        i += 1
    return poolidx if updated else False


def substitute(string, subidx, pool, poolidx):
    """
    Substitutes characters from pool into the given string. 
    """
    for (i, val) in enumerate(subidx):
        string = string[:val] + pool[poolidx[i]] + string[val + 1:]
    return string


if __name__ == "__main__":
    """
    Entry point. 
    """
    argp = get_args().parse_args()
    pool = get_pool(argp)
    subidx = get_subindex(argp.input, argp.subchar[0])
    poolidx = [0] * len(subidx)
    counter = 1
    out = sys.stdout if not argp.out else open(argp.out, "w+")

    start = datetime.now()
    print(substitute(argp.input, subidx, pool, poolidx), file=out)
    poolidx = increment_idx(poolidx, len(pool) - 1)
    while poolidx:
        print(substitute(argp.input, subidx, pool, poolidx), file=out)
        poolidx = increment_idx(poolidx, len(pool) - 1)
        counter += 1
    if argp.out:
        out.close()

    if argp.verb:
        print("[+] Total time taken: %s" %(datetime.now() - start))
        print("[+] Total words:      %s" %counter)
        print("[+] Pool size:        %s" %len(pool))

