#!/usr/bin/env python

import sys

def main(rowlen,redminlen):
    x = 2**rowlen
    i = 0
    n = 0
    while i<x:
        b = bin(i)[2:]
        for rl in range(1,redminlen):
            notallowed = '0'+'1'*rl+'0'
            srchin = '0'+b+'0'
            if srchin.find(notallowed) != -1: break
        else:
            #fullb = '0'*(rowlen-len(b)) + b
            n += 1
            #print n, fullb
            if n%1000 == 0: print n,
        i += 1
    print ""
    return n
        

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        print "error : wrong number of arguments"
        sys.exit(-1)
    rowlen, redminlen = int(args[0]), int(args[1])
    n = main(rowlen,redminlen)
    print "%s possibilities with rowlen=%s and minredlen=%s"%(n,rowlen,redminlen)

# ./114-binary.py 7 3

