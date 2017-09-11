#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
from time import ctime,sleep
import os
import sys
from mutil_test import get_info,manage_server
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')
rootpath = sys.path[0]


def run(arg):
    os.system(str(arg))

lprocess = []
ipadress = get_info.get_ip()
wdhost='http://{0}:'.format(ipadress)
arglist = sys.argv

if "-h" in arglist:
  outstr='''
    how to use it
    -h   help
    -s   the testsuites,likes 'suite1,suite2',split by ,
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

if "-path" in arglist:
    path=arglist[arglist.index('-path')+1]
else:
    print  'using delaut path "%s\\testcase"'%rootpath
    path=rootpath+r'\\testcase'
    # print  'using delaut path "testcase"'
    # path = "testcase"
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

taglist=tags.split(',')
tags = ''
for one in taglist:
    tags = tags + '-i ' + one + ' '

suiteslist = testsuites.split(',')
suites = ''
for one in suiteslist:
    suites = suites + '-s ' + one + ' '

i=0
sd=int(startd)-1
divtmp=get_info.get_devices()
divlist=divtmp[sd:]


currentpath = rootpath + "\\LogOutput\\TestResult\\"
if os.path.isdir(currentpath):
    shutil.rmtree(currentpath)
sleep(1)
os.mkdir(currentpath)
cmd3 = u"rebot --logtitle WhaleyVRApp_TestLog --reporttitle WhaleyVRApp_TestReport --output output.xml -d {0} ".format(currentpath)

for one in range(len(divlist)):
  wdport=wdhost+str(aport)+"/wd/hub"
  booll = manage_server.check_appium(ipadress, aport)
  if booll == 0:
      print "the appium server by port:{0} is not start,please check it".format(wdport)
      sys.exit(0)
  devicename = get_info.get_devicename(divlist[i])
  cmd = u'pybot --pythonpath . {0} {1} -d {5} -o resultDir_{4}\\output-of-{4}.xml -l resultDir_{4}\\log-of-{4}.html -r resultDir_{4}\\report-of-{4}.html --variable remote_url:{2} --variable udid:{3} {6}'.format(tags, suites, wdport, divlist[i], devicename, currentpath, path)
  cmd3 = cmd3 + u'{1}resultDir_{0}\\output-of-{0}.xml '.format(devicename,currentpath)
  p=multiprocessing.Process(target=run,args=(cmd,))
  lprocess.append(p)
  aport=aport+1
  i=i+1

if __name__ == '__main__':

    for p in lprocess:
        p.daemon = True
        p.start()

    for p in lprocess:
        p.join()

    os.system(cmd3)
    sleep(2)
    print "test finished"