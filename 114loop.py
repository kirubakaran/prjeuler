#!/usr/bin/env python

import sys

print "euler-114 loop"

def main(rowlen,redminlen):
    n = 0
    for redlen in range(1,rowlen):
        for origin in range(0,rowlen-redlen):
            
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

