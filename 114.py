#!/usr/bin/env python

import sys

print "euler-114"

def n_for_one_redlen(rowlen,redlen,n=0):
    return n

def main(rowlen,redminlen):
    n = 0
    r = redminlen
    while True:
        n += n_for_one_redlen(rowlen,r)
        if n == 0:
            break
        r += 1
    return n
        

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        print "error : wrong number of arguments"
        sys.exit(-1)
    n = main(*args)
    print "%s possibilities with rowlen=%s and minredlen=%s"%(n,args[0],args[1])

# ./114.py 7 3

