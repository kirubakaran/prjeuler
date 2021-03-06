#!/usr/bin/env python

import sys

print "euler-114"

def n_for_one_redlen(rowlen,redlen):
    if rowlen < redlen:
        return 0
    else:
        return 1 + n_for_one_redlen(rowlen-1,redlen)

def main(rowlen,redminlen):
    n = 0
    r = redminlen
    while True:
        nn = n_for_one_redlen(rowlen,r)
        if nn == 0:
            break
        n += nn
        r += 1
    return n
        

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        print "error : wrong number of arguments"
        sys.exit(-1)
    rowlen = int(args[0])
    redminlen = int(args[1])
    n = main(rowlen,redminlen)
    print "%s possibilities with rowlen=%s and minredlen=%s"%(n,args[0],args[1])

# ./114.py 7 3

