#!/usr/bin/env python
#coding:utf-8
import os
import sys
PATH=sys.path[0]+"/"
text=open(PATH+"target.txt",'r')
for line in text:
    print line
    os.system("python "+PATH+"exp.py -url "+line)