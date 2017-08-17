#!/usr/bin/env python
# -*- coding: utf-8 -*-
from AppiumExtend import *
import subprocess
from robot.api import logger
from appium import webdriver
from time import sleep
import os
import threading
import multiprocessing

__mtime__ = '2017/8/7'
class launchManagement(AppiumExtend):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        AppiumExtend.__init__(self)

    def getProjectRootPath(self):
        """get rootpath of project
        """
        rootpath = os.getcwd().split('\libs')[0]
        return rootpath

    def getDeviceList(self):
        p = subprocess.Popen("adb devices", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
        outter,err = p.communicate()
        devicesIds = []
        rootpath = self.getProjectRootPath() +r'devicesinfo.txt'
        with open(rootpath,"w") as f:
            outter = outter.decode('cp936').decode('utf-8')
            outter =  outter.split("\r\n")[1:]
            for one in outter:
                if one:
                    one = one.split('\tdevice')[0]
                    f.write(one + ',')
                    devicesIds.append(one)
        p.wait()
        return devicesIds

    def getCapabilities(self):
        devicelist = self.getDeviceList()
        apppath = self.getProjectRootPath() + r"\app\WhaleyVR.apk"
        port = 4721
        bootstrapport = 4722
        dict = {}
        for one in range(len(devicelist)):
            udid = devicelist[one]
            port += 2
            bootstrapport = bootstrapport + 2
            if udid == 'ea08a98e':
                devicename = 'MI5'
            elif udid == '8d5cd6c0':
                devicename = 'vivo x9i'
            elif udid == '6221231716B0904714':
                devicename =  '360'
            elif udid == '5e321b32':
                devicename = 'SamsungGalaxy7'
            elif udid == 'VGYP7T6P99999999':
                devicename = 'oppe r9tm'
            elif udid == 'GWY0217115007494':
                devicename = 'HUAWEI Meta9'
            try:
                desired_caps = {
                    'platformName':'Android',
                    'deviceName' :devicename,
                    'app' : apppath,
                    'appPackage' : 'com.snailvr.manager',
                    'appActivity' : 'com.whaley.vr.module.launcher.activitys.SplashActivity',
                    'unicodeKeyborad' : True,
                    'resetKeyborad' : True,
                    'noRest' : True,
                    'commandTimeout': 60,
                    'autoGrantPermissions':True,
                    'sessonOverride': True
                }
            except UnboundLocalError:
                print   'devicename not found'
            remote_server = 'http://127.0.0.1:%s/wd/hub' % port
            if udid not in dict:
                dict[udid] = {'remote_server':remote_server,'desired_caps':desired_caps,'port':port,'bootstrapport':bootstrapport,'udid':udid}
            else:
                dict[udid].append({'remote_server':remote_server,'desired_caps':desired_caps,'port':port,'bootstrapport':bootstrapport,'udid':udid})
        return dict

    def start_servers(self,port,bootstrapport,udid):
        sleep(5)
        cmd = r'node C:\Users\dell\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\build\lib\main.js -a 127.0.0.1 -p %s -bp %s -U %s --session-override'%(port,bootstrapport,udid)
        # os.system(cmd)
        subprocess.Popen(cmd,shell=True)
        sleep(5)

    def kill_node(self):
        for one in range(len(self.getDeviceList())):
            port = 4723
            cmd = 'netstat -ano|findstr "%s"'%port
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out,err=p.communicate()
            if out:
                out = out.split('\r\n')[0].split(' ')[-1]
                kill = 'taskkill /pid %s /F'%out
                subprocess.Popen(kill,shell=True)
            port += 2
            continue

    def open_applications(self,lock,remote_server,desired_caps,udid,alias=None):
        lock.acquire()
        try:
            thraed0 = threading.Thread(target=self.install_alert,args=(udid,))
            thraed0.start()
            application = webdriver.Remote(command_executor=remote_server, desired_capabilities=desired_caps)
            self._debug('Opened application with session id %s' % application.session_id)
            return self._cache.register(application,alias)
        finally:
            lock.release()
        # driver.find_element_by_id("com.snailvr.manager:id/iv_leapfrog").click()
        # driver.find_element_by_id("com.snailvr.manager:id/tv_user").click()
        #
        # driver.find_element_by_id("com.snailvr.manager:id/iv_setting").click()
        # for one in range(10):
        #     driver.find_element_by_id("com.snailvr.manager:id/btn_back").click()
        #     driver.find_element_by_id("com.snailvr.manager:id/iv_setting").click()

    def install_alert(self,udid):
        """create function using for dealing with alert during install the app
        """
        watcherpath = self.getProjectRootPath() + r"\libs\UIWatcher.jar"
        cmd1 = "adb -s %s push "%udid + watcherpath + " data/local/tmp"
        push = subprocess.Popen(cmd1,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        cmd2 = "adb -s %s shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers"%udid
        run = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        outter, err = push.communicate()
        outter1, err1 = run.communicate()
        # logger.console(outter)
        print outter1
        sleep(5)
        # logger.console(outter1)


    def multitest(self):
        dict = self.getCapabilities()
        lock = multiprocessing.Lock()
        for one in dict:
            port = dict[one]['port']
            bootstrapport = dict[one]['bootstrapport']
            udid = dict[one]['udid']
            remote_server = dict[one]['remote_server']
            desired_caps = dict[one]['desired_caps']
            thread = threading.Thread(target=self.start_servers(port,bootstrapport,udid))
            thread.start()
            process1 = multiprocessing.Process(target=self.open_applications,args=(lock,remote_server,desired_caps,udid))
            process1.start()






