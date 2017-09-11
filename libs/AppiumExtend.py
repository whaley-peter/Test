#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from AppiumLibrary import *
from eles.loginpage import *
from eles.minepage import *
from eles.homepage import *
from appium import webdriver
from robot import utils
from robot.api import logger
from eles.globaleles import *
import subprocess
import threading
import multiprocessing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import shutil
from mutil_test import get_info

reload(sys)
sys.setdefaultencoding('utf-8')

# set default timeout
TIMEOUT = 15

class AppiumExtend(AppiumLibrary):

    ROBOT_LIBRARY_SCOPE = 'Global'
    localTime = time.strftime("%Y-%m-%d", time.localtime())

    def __init__(self):
        AppiumLibrary.__init__(self)

    def install_alert(self,udid=None):
        watcherpath = getProjectRootPath() + r"\libs\UIWatcher.jar"
        if udid==None:
            cmd1 = "adb push " + watcherpath + " data/local/tmp"
            cmd2 = u"adb shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers"
        else:
            cmd1 = 'adb -s {0} push '.format(udid) + watcherpath + " data/local/tmp"
            cmd2 = u"adb -s {0} shell uiautomator runtest UIWatcher.jar -c com.whaleytest.UiWatchers".format(udid)

        push = subprocess.Popen(cmd1,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        run = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        outter, err = push.communicate()
        outter1, err1 = run.communicate()
        logger.console(outter)
        logger.console(outter1)

    def open_application(self, remote_url,desired_caps,alias=None):
        """Opens a new application to given Appium server.
        Capabilities of appium server, Android and iOS,
        Please check http://appium.io/slate/en/master/?python#appium-server-capabilities
        | *Option*            | *Man.* | *Description*     |
        | remote_url          | Yes    | Appium server url |
        | alias               | no     | alias             |
        Examples:
        | Open Application | http://localhost:4723/wd/hub | alias=Myapp1         | platformName=iOS      | platformVersion=7.0            | deviceName='iPhone Simulator'           | app=your.app                         |
        | Open Application | http://localhost:4723/wd/hub | platformName=Android | platformVersion=4.2.2 | deviceName=192.168.56.101:5555 | app=${CURDIR}/demoapp/OrangeDemoApp.apk | appPackage=com.netease.qa.orangedemo | appActivity=MainActivity |
        """
        self.kill_uiautomator()
        preinstallThread = threading.Thread(target=self.install_alert)
        preinstallThread.start()

        application = webdriver.Remote(str(remote_url), desired_caps)
        self._debug('Opened application with session id %s' % application.session_id)

        return self._cache.register(application, alias)

    def open_mutilapplications(self,remote_url,udid,alias=None):
        """a method used for mutil test

        | open mutilapplications | ${remote_url} | ${udid} |
        """
        apppath1 = r"D:\Jenkins\workspace\AndroidCIT\WhaleyVR\launcher\build\outputs\apk\launcher-debug.apk"
        # apppath1 = r"e:\Test1\launcher-debug.apk"
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'test',
            'udid': udid,
            'app': apppath1,
            'appPackage': 'com.snailvr.manager',
            # 'appActivity': 'com.whaley.vr.module.launcher.activitys.SplashActivity',
            'appActivity': 'com.whaley.biz.launcher.activitys.LauncherActivity',
            'unicodeKeyborad': True,
            'resetKeyborad': True,
            'noReset': True,
            'commandTimeout': 60,
            'autoGrantPermissions': True,
            'sessonOverride': True
        }
        self.kill_uiautomator(udid)
        thraed0 = threading.Thread(target=self.install_alert, args=(udid,))
        thraed0.start()

        application = webdriver.Remote(remote_url, desired_caps)
        self._debug('Opened application with session id %s' % application.session_id)

        return self._cache.register(application, alias)

    def kill_uiautomator(self,udid=None):
        """kill uiautomator after test
        for mutil test,you must put the udid Variables

        :param udid:
        :return:
        Example:
        | kill uiautomator |
        | kill uiautomator | ${udid} |
        """
        time.sleep(5)
        if udid == None:
            cmd = "adb shell ps |find " + r'"uiautomator"'
        else:
            cmd = "adb -s {0} shell ps |find " + r'"uiautomator"'.format(udid)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        if out:
            a = out.split(" ")[5]
            if udid == None:
                kill = "adb shell kill " + a
            else:
                kill = "adb -s {0} shell kill ".format(udid) + a
            killinfo = subprocess.Popen(kill, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            killout,killerr= killinfo.communicate()
            if killout:
                logger.console(killout)
            else:
                logger.console(killerr)

    def login(self,username=username,password=password):
        """login app

        Example:
        | login |
        | login | 18616512272 | a123456 |
        """
        login = 'id='+loginbutton
        nickname1 = 'id=' + nickname
        leapforg1 = "id=" +leapfrog
        self.back_to_homepage()
        def login_app():
            self.click_element(login)
            locator1 = 'id=' + usernameinput
            locator2 = 'id=' + passwordinput
            self.input_text(locator1, username)
            self.input_text(locator2, password)
            self.click_element(loginbutton)
            self.wait_until_element_is_visible('id=' + homebase)

        if self.is_element_present(leapforg1):
            login_app()
        else:
            self.back_to_homepage()
            self.click_element("id="+mybase)
            if not self.is_element_present(nickname1):
                login_app()
            else:
                print "app already login"

    def skip_login(self):
        try:
            self.click_element_until_no_error("id="+leapfrog)
            # self.click_element('id='+leapfrog)
        except :
            raise   logger.console("can't find element by given locator %s"%leapfrog)

    def logout(self):
        """logout app

        :return:
        Example:
        | logout |
        """
        self.back_to_homepage()
        nickname1 = 'id=' + nickname
        try:
            self.click_element("id="+mybase)
            if self.is_element_present(nickname1):
                self.click_element("id="+settingbutton)
                self.click_element("id="+logoutbutton)
                self.click_element("id=" + confirmbutton)
        except:
            raise self._info("can't find element by given locator %s or %s or %s or %s"%(mybase,settingbutton,logoutbutton, confirmbutton))

    def switch_to_debug_mode(self,udid=None):
        """swith the app to debug mode
        for mulittest you maust set the udid Variables
        Example:
        | swith to debug mode |
        | swith to debug mode | ${udid} |
        """
        self.back_to_homepage()
        self.wait_until_element_is_visible("id=" + mybase,10)
        self.click_element("id=" + mybase)
        self.click_element("id=" + settingbutton)
        debugbutton = "xpath=" + debugswitch
        debug = self.get_text(debugbutton)
        if debug == u'是':
            self.back_to_homepage()
        else:
            self.click_element(debugbutton)
            self.go_back()
            self.go_back()
            self.go_back()
            if udid == None:
                cmd = "adb shell am start -n com.snailvr.manager/com.whaley.biz.launcher.activitys.LauncherActivity"
            else:
                cmd = "adb -s %s shell am start -n com.snailvr.manager/com.whaley.biz.launcher.activitys.LauncherActivity"%udid
            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(TIMEOUT)

    def login_and_switch_to_debug_mode(self,username=username,password=password,udid=None):
        """login app adn swith app to debugmode
        if loginOrnot is False,then swith app to debugmode without login

        Examples:
        | login and swith to debug mode |
        | login and swith to debug mode | 18616512272 | a123456 |
        """
        self.login(username,password)

        self.switch_to_debug_mode(udid)

    def skip_login_and_switch_to_debug_mode(self,message="",timeout=TIMEOUT):
        """skip login app and swith to debug mode

        :param message:
        :param timeout:
        :return:
        Example:
        | skip login and swith to debug mode |
        """
        self.skip_login()
        self.switch_to_debug_mode()
        locator = 'id='+leapfrog
        self._wait_until_no_error_fixed(timeout,True,message,self.click_element,locator)

    def back_to_homepage(self,message="",timeout=TIMEOUT):
        """click backbutton go back to homepage using for setup or treadown test

        Example:
        | back to homepage |
        """
        locator = "id=" + backbutton
        while True:
            if self.is_element_present("id="+homebase):
                break
            elif not self.is_element_present("id="+homebase) and self.is_element_present(locator):
                self._wait_until_no_error_fixed(timeout, True, message, self.click_element, locator)
                continue
            elif not self.is_element_present("id="+homebase) and not self.is_element_present(locator):
                if self.is_element_present('id='+loginbutton):
                    break
                self._current_application().back()
                continue

    def click_back_nth(self,nth=1,message="",timeout=TIMEOUT):
        """click backbutton nth times
        :param nth:
        :param message:
        :param timeout:
        :return:
        Example:
        | click back nth | 2 |

        """
        locator = "id=" + backbutton
        nth = int(nth)
        for one in range(nth):
            if self.is_element_present(locator):
                self._wait_until_no_error_fixed(timeout,True,message,self.click_element,locator)
            elif not self.is_element_present(locator) and not self.is_element_present("id="+homebase):
                self._current_application().back()
            elif not self.is_element_present(locator) and self.is_element_present("id="+homebase):
                break


    # def check_toast(self,toasttext):
    #     """check whether the toast of element is the same as the giving one
    #
    #     :param toasttext:
    #     :return:
    #     Example:
    #     | check toast | 加入播单成功 |
    #     """
    #     toasttext = str(toasttext)
    #     message = '//*[@text=\'%s\']'%toasttext
    #     element = WebDriverWait(self._current_application(),10).until(EC.presence_of_element_located((By.XPATH,message)))
    #     try:
    #         if element.text == toasttext:
    #             self._info('find toast and matched')
    #         else:
    #             raise self._info('toast does not match with the giving one')
    #     except:
    #         raise  AssertionError('element does not find exception')

    # def input_text(self, locator,text,udid=None):
    #     """override the input text method to fix problem of sendkeys function in appium+uiautomator2
    #         udid is required for mutil test
    #     :param locator:
    #     :param text:
    #     :return:
    #     Example:
    #     | input text | id=${passwordinput} | a123456 |
    #     | input text | id=${passwordinput} | a123456 | ${udid} |
    #     """
    #     time.sleep(1)
    #     self.click_element_until_no_error(locator)
    #     time.sleep(1)
    #     if udid==None:
    #         cmd = 'adb shell input text {0}'.format(text)
    #     else:
    #         cmd = 'adb -s {0} shell input text {1}'.format(udid,text)
    #     subprocess.Popen(cmd,shell=True)
    #     time.sleep(1)
    def logcat(self,udid=None,testcasename=None):
        self.kill_logcat(udid)
        devicename = get_info.get_devicename(udid)
        path = getProjectRootPath().split("\libs")[0]
        if udid==None:
            dir= "{0}/LogOutput/Temp".format(getProjectRootPath().split("\libs")[0])
        else:
            dir = "{0}/LogOutput/Temp_{1}".format(getProjectRootPath().split("\libs")[0],devicename)
        if os.path.isdir(dir):
            shutil.rmtree(dir)
        os.mkdir(dir)
        if udid==None and testcasename==None:
            logcat = r'start {0}/mutil_test/logcat_noPar.bat {0}'.format(path)
        elif udid!=None and testcasename != None:

            logcat = r'start {1}/mutil_test/logcat.bat {0} {1} {2} {2} {3}'.format(udid, path,devicename,testcasename)

        subprocess.Popen(logcat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


    def kill_logcat(self,udid=None):
        if udid == None:
            cmd = "adb shell ps |find " + r'"logcat"'
        else:
            cmd = "adb -s {0} shell ps |find ".format(udid) + r'"logcat"'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out,err = p.communicate()
        print out
        print err
        while out:
            lines = out.split("\r\n")
            for line in lines:
                if line:
                    pid = line.split()[1]
                    if udid == None:
                        kill = "adb shell kill " + pid
                    else:
                        kill = "adb -s {0} shell kill ".format(udid) + pid
                    os.system(kill)
            break

    def save_log(self,udid=None):
        time.sleep(1)
        self.kill_logcat(udid)
        devicename = get_info.get_devicename(udid)
        if udid==None:
            dir= "{0}/LogOutput/Temp/".format(getProjectRootPath().split("\libs")[0])
        else:
            dir= "{0}/LogOutput/Temp_{1}/".format(getProjectRootPath().split("\libs")[0],devicename)

        if not os.path.isdir(dir):
            os.mkdir(dir)
        alllist = os.listdir(dir)
        for one in alllist:
            aa,bb= one.split(".")
            file = dir+aa+"."+bb
            newpath = "{0}/LogOutput/Logcat/".format(getProjectRootPath().split("\libs")[0])
            newfile = "{0}/LogOutput/Logcat/{1}.{2}".format(getProjectRootPath().split("\libs")[0],aa,bb)
            if not os.path.isdir(newpath):
                os.mkdir(newpath)
            shutil.copyfile(file,newfile)
        shutil.rmtree(dir)
        os.mkdir(dir)

    def delete_nth_element(self,nth=1):
        """delete nth element on the page

        :param nth:
        :return:
        Example:
        | delete nth element | 2 |
        | delete nth element |
        """
        try:
            nth = int(nth)
        except ValueError, e:
            raise ValueError(u"'%s' is not a number" % nth)
        if nth == 0:
            raise ValueError(u"'nth' must not equal 0")

        if not self.is_element_present("id=" + mycollectionempty) or self.is_element_present("id=" + localempty):
            self.click_element_until_no_error("id="+bianji)
            elements = self.get_webelements(check)

            if nth > 0:
                elements[nth - 1].click()
            elif nth < 0:
                elements[nth].click()
            if self.is_element_present("id="+delete):
                self.click_element_until_no_error("id="+delete)
            elif self.is_element_present("id=com.snailvr.manager:id/tv_delete"):
                self.click_element_until_no_error("id=com.snailvr.manager:id/tv_delete")
            self.click_element_until_no_error("id="+confirm)
        else:
            logger.console("no element to deleting")

    def delete_all_element(self):
        """delete all element of page,before delete check whether user can cancle delete
        :return:
        Example:
        | delete all element |
        """
        if not self.is_element_present("id="+mycollectionempty) or self.is_element_present("id="+localempty):
            self._current_application().find_element_by_id(bianji).click()
            checkall1 = "id=" + checkall
            if self.is_element_present(checkall1):
                self.click_element_until_no_error(checkall)
                self.is_all_selected()
                self.click_element_until_no_error("id="+delete)
                self.click_element_until_no_error("id="+quxiao)
                self.click_element_until_no_error("id="+delete)
            else:
                self.click_element_until_no_error("id=com.snailvr.manager:id/tv_check")
                self.is_all_selected()
                self.click_element_until_no_error("id=com.snailvr.manager:id/tv_delete")
                self.click_element_until_no_error("id="+quxiao)
                self.click_element_until_no_error("id=com.snailvr.manager:id/tv_delete")

            self.click_element_until_no_error("id=" + confirm)
        else:
            logger.console("no element to deleting")

    def is_all_selected(self,message=""):
        """check whether all element is selected

        :return:
        Exapmle:
        |     is all selected |
        """
        locator = "id=com.snailvr.manager:id/tv_delete"
        locator1 = "id=com.snailvr.manager:id/tv_check_num"
        if self.is_element_present(locator):
            select = self.get_text(locator).split("(")[1].split(")")[0].split("/")[0]
            all = self.get_text(locator).split("(")[1].split(")")[0].split("/")[1]
        elif self.is_element_present(locator1):
            select = self.get_text(locator1).split("(")[1].split(")")[0].split("/")[0]
            all = self.get_text(locator1).split("(")[1].split(")")[0].split("/")[1]

        if select != all:
            if not message:
                message = "select element is %s,but all element is %s" % (select, all)
            raise AssertionError(message)
        else:
            self._info("selected and all elemets are equal")

    def getsize(self):
        """get the max X,Y coordinate of srceen

        """
        x = self._current_application().get_window_size()['width']
        y = self._current_application().get_window_size()['height']
        return x,y

    def swipe_up_nth(self,nth=1):
        """swipe the screen up nth times

        Exapmles:
        | swipe up nth |
        | swipe up nth | 2 |
        """
        size = self.getsize()
        x1 = int(size[0]*0.5)
        y1 = int(size[1]*0.75)
        y2 = int(size[1]*0.25)
        nth = int(nth)
        for one in range(nth):
            self._current_application().swipe(x1,y1,x1,y2,1000)
            time.sleep(1)

    def swipe_up_until_element_presented(self,locator):
        try:
            while True:
                if not self.is_element_present(locator):
                    self.swipe_up_nth()
                    continue
                else:
                    break
        except:
            raise logger.debug('element cnanot found by given %s'%locator,True)

    def swipe_down_nth(self,nth=1):
        """swipe the screen down nth times

        Exapmles:
        | swipe dowm nth |
        | swipe woen nth | 2 |
        """
        size = self.getsize()
        x1 = int(size[0]*0.5)
        y1 = int(size[1]*0.25)
        y2 = int(size[1]*0.75)
        nth = int(nth)
        for one in range(nth):
            self._current_application().swipe(x1,y1,x1,y2,1000)
            time.sleep(1)

    def swipe_down_until_element_presented(self,locator):
        try:
            while True:
                if not self.is_element_present(locator):
                    self.swipe_down_nth()
                    continue
                else:
                    break
        except:
            raise logger.debug('element cnanot found by given %s'%locator,True)

    def swipe_left_nth(self,nth=1):
        """swipe the screen left nth times
        Exapmles:
        | swipe left nth |
        | swipe left nth | 2 |
        """
        size = self.getsize()
        x1 = int(size[0]*0.75)
        y1 = int(size[1]*0.6)
        x2 = int(size[0]*0.05)
        nth = int(nth)
        for one in range(nth):
            self._current_application().swipe(x1,y1,x2,y1,1000)
            time.sleep(1)

    def swipe_right_nth(self,nth=1):
        """swipe the screen right nth times
        Exapmles:
        | swipe right nth |
        | swipe right nth | 2 |
        """
        size = self.getsize()
        x1 = int(size[0]*0.05)
        y1 = int(size[1]*0.6)
        x2 = int(size[0]*0.75)
        nth = int(nth)
        for one in range(nth):
            self._current_application().swipe(x1,y1,x2,y1,1000)
            time.sleep(1)


    def input_until_no_error(self, locator, text, message="", timeout=TIMEOUT):
        """Try types the given `text` into text field identified by `locator` until no error occurred.

        Fails if `timeout` expires before the input success.

        Examples:
        | Input Until No Error | class=android.widget.Button | username |                |     |
        | Input Until No Error | class=android.widget.Button | username | input username | 10s |
        """
        if not message:
            message = "Typing text '%s' into text field '%s'" % (text, locator)
        self._wait_until_no_error_fixed(timeout, True, message, self.input_text, locator, text)

    def clear_until_no_error(self, locator, message="", timeout=TIMEOUT):
        """Try clear `text` in text field identified by `locator` until no error occurred.

        Fails if `timeout` expires before the clear success.

        Examples:
        | Clear Until No Error |               |                |     |
        | Clear Until No Error | name=username | clear username | 10s |
        """
        if not message:
            message = "Clear text field '%s'" % locator
        self._wait_until_no_error_fixed(timeout, True, message, self.clear_text, locator)

    def click_element_until_no_error(self, locator, message="", timeout=TIMEOUT):
        """Try click element identified by `locator` until no error occurred.

        Fails if `timeout` expires before the click success.

        Examples:
        | Click Until No Error | name=Login |           |     |
        | Click Until No Error | name=Login | click btn | 10s |
        """
        if not message:
            message = "Clicking element '%s'" % locator
        self._wait_until_no_error_fixed(timeout, True, message, self.click_element, locator)

    def click_nth_element(self, locator, nth=1):
        """Click the nth element identified by `locator`.

        Examples:
        | #Click the 2th element |                             |    |
        | Click Nth Element      | class=android.widget.Button |  2 |
        | #Click last element    |                             |    |
        | Click Nth Element      | class=android.widget.Button | -1 |
        """
        try:
            nth = int(nth)
        except ValueError, e:
            raise ValueError(u"'%s' is not a number" % nth)
        if nth == 0:
            raise ValueError(u"'nth' must not equal 0")
        elements = self.get_webelements(locator)
        self._info("Clicking %dth element '%s'" % (nth, locator))
        if nth > 0:
            elements[nth - 1].click()
        elif nth < 0:
            elements[nth].click()

    def click_nth_element_until_no_error(self, locator, nth=1, message="", timeout=TIMEOUT):
        """Click the nth element identified by `locator` until no error occurred.

        Fails if `timeout` expires before the click success.

        Examples:
        | #Click the 2th element   |                             |    |                |     |
        | Click Nth Until No Error | class=android.widget.Button |  2 |                |     |
        | #Click last element      |                             |    |                |     |
        | Click Nth Until No Error | class=android.widget.Button | -1 | click last btn | 10s |
        """
        if not message:
            message = "Clicking %sth element '%s'" % (nth, locator)
        self._wait_until_no_error_fixed(timeout, True, message, self.click_nth_element, locator, nth)

    def click_until_waitElement_exists(self, locator, wait_locator, message="", timeout=TIMEOUT):
        """Click element identified by `locator` until element identified by `wait_locator` appear.

        Fails if `timeout` expires before element identified by `wait_locator` appear.

        Examples:
        | Click Until Element Exists | name=first | name=twice |                                    |     |
        | Click Until Element Exists | name=first | name=twice | Click 'first' until 'twice' appear | 10s |
        """
        if not message:
            message = "Clicking element '%s' until element '%s' appear" % (locator, wait_locator)

        def click_if_not_exists():
            try:
                self.click_element(locator)
            except Exception:
                raise "cannot find element by '%s' or '%s' is not present"%(locator,wait_locator)
            self.page_should_contain_element(wait_locator)

        self._wait_until_no_error_fixed(timeout, True, message, click_if_not_exists)

    def click_nth_element_until_waitelement_exists(self, locator, nth, wait_locator, message="", timeout=TIMEOUT):
        """Click the nth element identified by `locator` until element identified by `wait_locator` appear.

        Fails if `timeout` expires before element identified by `wait_locator` appear.

        Examples:
        | Click Nth Until Element Exists | name=test1 |  2 | name=test2 |                                         |     |
        | Click Nth Until Element Exists | name=test1 | -1 | name=test2 | Click last 'test1' until 'test2' appear | 10s |
        """
        if not message:
            message = "Clicking %sth element '%s' until element '%s' appear" % (nth, locator, wait_locator)

        def click_nth_if_not_exists():
            try:
                self.click_nth_element(locator, nth)
            except Exception as e:
                raise e
            self.page_should_contain_element(wait_locator)

        self._wait_until_no_error_fixed(timeout, True, message, click_nth_if_not_exists)

    def scroll_continue_no_error(self, locator_list, message=""):
        """Scrolls from one element to another.

        Do not raise error if any step failed.

        Examples
        | Scroll Continue No Error | name=first,name=twice,name=third |                            |
        | Scroll Continue No Error | name=first,name=twice,name=third | Scroll first->twice->third |
        """
        if not isinstance(locator_list, list):
            _locator_list = self._convert_to_list(locator_list)
        if not message:
            message = "Scrolling [%s]" % ("->".join(_locator_list))
        flag = True
        for index in range(len(_locator_list) - 1, 0, -1):
            try:
                self.scroll(_locator_list[index - 1], _locator_list[index])
            except:
                flag = False
                continue
        if flag:
            self._info(u"%s ==> PASS." % (message))
        else:
            self._info(u"%s ==> NOT ALL PASS." % (message))

    def click_if_exists_in_time(self, locator, message="", timeout=TIMEOUT):
        """Try click element identified by `locator` in setting time.

        Ignore if `timeout` expires before the click success.

        Examples:
        | Click If Exists In Time | name=skip |                                    |     |
        | Click If Exists In Time | name=skip | click skip, no error if click fail | 10s |
        """
        if not message:
            message = "Clicking element '%s'" % locator
        return self._wait_until_no_error_fixed(timeout, False, message, self.click_element, locator)

    def double_click_element(self, locator):
        """Try double click element identified by 'locator'

        Examples:
        | Double click element | name=login |
        """

        try:
            self.click_element(locator)
            time.sleep(1)
            self.click_element(locator)
        except Exception:
            raise "element cannot found by '%s'" %locator

    def double_click_until_no_error(self, locator, message="", timeout=TIMEOUT):
        """Try double click element identified by `locator` until no error occurred.

        Fails if `timeout` expires before the click success.

        Examples:
        | Double Click Until No Error | name=Login |                         |     |
        | Double Click Until No Error | name=Login | double click login link | 10s |
        """

        if not message:
            message = "Double clicking element '%s'" % locator
        self._wait_until_no_error_fixed(timeout, True, message, self.double_click_element(locator), locator)

    def is_element_present(self, locator):
        """Check the element identified by `locator` is exist or not.

        Return True if locator element present, False if locator element not present.

        Examples:
        | ${isPresent}= | Is Element Present | name=Login |
        """
        time.sleep(2)
        return self._is_element_present(locator)

    def get_nth_element_text(self, locator, nth=1):
        """find text of nth element by `locator`. return a text

        Examples:
        | get nth element text | id=com.snailvr.manager:id/name | 2 |
        | ${val} | get nth element text | id=com.snailvr.manager:id/name | 2 |
        """
        try:
            nth = int(nth)
        except ValueError, e:
            raise ValueError(u"'%s' is not a number" % nth)
        if nth == 0:
            raise ValueError(u"'nth' must not equal 0")
        elements = self.get_webelements(locator)
        self._info("get %dth element '%s' 's text" % (nth, locator))
        if nth > 0:
            return self.get_text(elements[nth - 1])
        elif nth < 0:
            return self.get_text(elements[nth])

    def get_element_attribute_in_time(self, locator, attribute, message="", timeout=TIMEOUT):
        """Get element attribute using given attribute: name, value,... by `locator` until no error occurred.

        Fails if `timeout` expires before the click success.

        Examples:
        | Get Element Attribute In Time | id=com.xx/id/what | text |                  |     |
        | Get Element Attribute In Time | id=com.xx/id/what | text | get element name | 10s |
        """
        if not message:
            message = "Element locator '%s' did not match any elements." % locator
        return self._wait_until_no_error_fixed(timeout, True, message, self.get_element_attribute, locator, attribute)

    def get_element_count(self, locator):
        """Count elements found by `locator`.

        Examples:
        | ${count}= | Get Element Count | class=android.widget.Button |
        """
        return len(self.get_webelements(locator))

    def get_element_count_in_time(self, locator, message="", timeout=TIMEOUT):
        """Count elements found by `locator` until result is not 0.

        Return 0 if `timeout` expires.

        Examples:
        | ${count}= | Get Element Count In Time | class=android.widget.Button |              |     |
        | ${count}= | Get Element Count In Time | class=android.widget.Button | count button | 10s |
        """
        return self._wait_until_not_value(timeout, 0, False, message, self.get_element_count, locator)

    def page_should_contain_text_in_time(self, text, message="", timeout=TIMEOUT):
        """Verifies text is not found on the current page in setting time.

        Fails if `timeout` expires before find page contain text.

        Examples:
        | Page Should Contain Text In Time | hello world |            |     |
        | Page Should Contain Text In Time | hello world | check page | 10s |
        """
        if not message:
            message = "Page should have contained text '%s' in %s" % (text, self._format_timeout(timeout))
        self._wait_until_no_error_fixed(timeout, True, message, self.page_should_contain_text, text, 'NONE')

    def page_should_contain_element_in_time(self, locator, message="", timeout=TIMEOUT):
        """Verifies element identified by `locator` is not found on the current page in setting time.

        Fails if `timeout` expires before find page contain locator element.

        Examples:
        | Page Should Contain Element In Time | name=Login |                          |     |
        | Page Should Contain Element In Time | name=Login | check login button exist | 10s |
        """
        if not message:
            message = "Page should have contained element '%s' in %s" % (locator, self._format_timeout(timeout))
        self._wait_until_no_error_fixed(timeout, True, message, self.page_should_contain_element, locator, 'NONE')

    def wait_until_page_contains_elements(self, locator_list, message="", timeout=TIMEOUT):
        """Waits until any element specified with `locator_list` appears on current page.

        Return appear locator if found.
        Fails if `timeout` expires before the element appears.

        Examples:
        | Wait Until Page Contains Elements | name=unlogin, name=login          |                            |                       |     |
        | ${appear_locator}=                | Wait Until Page Contains Elements | [name=unlogin, name=login] | wait elements appears | 10s |
        """
        if not isinstance(locator_list, list):
            _locator_list = self._convert_to_list(locator_list)
        message_info = "Wait Page contains %s in %s" % (
        " or ".join(["'" + i + "'" for i in _locator_list]), self._format_timeout(timeout))
        if not message:
            message = message_info
        self._info(u"%s." % message_info)
        timeout = utils.timestr_to_secs(timeout) if timeout is not None else 15
        maxtime = time.time() + timeout
        while True:
            for locator in _locator_list:
                if self._is_element_present(locator):
                    self._info(u"%s ==> PASS." % message)
                    return locator
                else:
                    if time.time() > maxtime:
                        raise AssertionError(u"%s ==> FAIL." % message)

                continue
            break

    def _convert_to_list(self, str_list):
        if str_list.startswith('[') and str_list.endswith(']'):
            str_list = str_list[1:-1]
        return [i.strip() for i in str_list.split(',')]

    def _wait_until_no_error_fixed(self, timeout, fail_raise_error, message, wait_func, *args):
        timeout = utils.timestr_to_secs(timeout) if timeout is not None else 15
        maxtime = time.time() + timeout
        while True:
            try:
                res = wait_func(*args)
            except:
                timeout_error = True
            else:
                timeout_error = False
            if not timeout_error:
                self._info(u"%s ==> PASS." % message)
                return res
            if time.time() > maxtime:
                if not fail_raise_error:
                    self._info(u"%s ==> NOT PASS." % message)
                    return False
                else:
                    raise AssertionError(u"%s ==> FAIL." % message)
            break

    def _wait_until_not_value(self, timeout, value, fail_raise_error, message, wait_func, *args):
        timeout = utils.timestr_to_secs(timeout) if timeout is not None else 20
        maxtime = time.time() + timeout
        while True:
            res = wait_func(*args)
            if res != value:
                if message:
                    self._info(u"%s ==> %s." % (message, res))
                return res
            if time.time() > maxtime:
                if not fail_raise_error:
                    if message:
                        self._info(u"%s ==> %s." % (message, res))
                    return res
                if message:
                    raise AssertionError(u"%s ==> %s." % (message, res))
                else:
                    raise AssertionError(u"Return ==> %s." % res)
                break
            time.sleep(0.5)

if __name__=="__main__":
    a = AppiumExtend()
    for one in range(5):
        time.sleep(1)
        a.logcat("5e321b32","test1")
        # a.logcat()
        time.sleep(3)
        # print "kill========================"
        a.save_log("5e321b32")