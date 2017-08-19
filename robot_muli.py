#coding=utf-8
from libs.launchManagement import *
import threading
from time import ctime,sleep
import os
import multiprocessing

def run(arg):
   # subprocess.Popen(arg,shell=True)
   os.system(arg)

if __name__ == '__main__':
    kill_node()
    multi_servers_start()
    sleep(5)
    dict = getCapabilities()
    lock = multiprocessing.Lock()
    processes = []
    cmd3 = "rebot --logtitle WhaleyVRApp_TestLog --reporttitle WhaleyVRApp_TestReport "
    for one in dict:
        devicename = dict[one]['deviceName']
        cmd1 = "Start /wait pybot -o .\\resultDir_{0}\\output-of-{0}.xml -l .\\resultDir_{0}\\log-of-{0}.html -r .\\resultDir_{0}\\report-of-{0}.html --pythonpath . --test *testdenglu001 testcase &exit".format(devicename)
        cmd3 =  cmd3 + '.\\resultDir_{0}\\output-of-{0}.xml '.format(devicename)
        process = multiprocessing.Process(target=run, args=(cmd1,))
        with open('udid.txt','w') as f:
            f.write(one)
        process.start()
        # processes.append(process)
        sleep(10)
    # for process in processes:
    #     process.join()
    with open('outputReportcombine.bat','w') as combin:
        combin.write(cmd3)
    print 'test finshed'


