#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime, sleep
import os
import sys
import shutil
arglist = sys.argv

if "-h" in arglist:
  outstr='''
    how to use it
    -h   help
    -s   the testsuites,likes 'suite1,suite2',split by,
    -t   taglist,likes "tag1,tag2", split by ,
    -path path to start the test
    -p   server port
    -sp  second server port
  '''
  print outstr
  sys.exit(0)

if "-s" in arglist:
  testsuites=arglist[arglist.index('-s')+1]
else:
  print  'using delaut suite "testcase"'
  testsuites='testcase'

if "-t" in  arglist:
  tags=arglist[arglist.index('-t')+1]
else:
  print "if you want to run test by mutil,you can input like this : -t node1,node2"
  tags=[]

if "-d" in  arglist:
  startd=arglist[arglist.index('-d')+1]
else:
  startd=1

if "-p" in arglist:
    aport=int(arglist[arglist.index('-p')+1])
    iport=int(arglist[arglist.index('-p')+1])
else:
    aport=4723
    iport=14723

if "-sp" in arglist:
    bport=int(arglist[arglist.index('-sp')+1])
    wport=int(arglist[arglist.index('-sp')+1])
else:
    bport=5723
    wport=8101

currentpath = sys.path[0]

run_server = r"python {0}\run_server.py".format(currentpath)
run_test = r"python {3}\robot_mutil_test.py -t {0} -s {1} -p {2}".format(tags,testsuites,aport,currentpath)


LogOutputfile = currentpath + "\\LogOutput\\"
if os.path.isdir(LogOutputfile):
    shutil.rmtree(LogOutputfile)
os.mkdir(LogOutputfile)

os.system(run_server)
sleep(5)
os.system(run_test)