#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/9'

from appium import webdriver
from time import sleep
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from eles.globaleles import getProjectRootPath
from libs.AppiumExtend import *
from eles.minepage import *
reload(sys)
sys.setdefaultencoding('utf-8')

desired_caps = {
    'platformName':'Android',
    # 'platformVersion' : '6.0.1',
    'deviceName' :'test',
    # 'udid':'8d5cd6c0',
    'app' : r'E:\Test\app\WhaleyVR.apk',
    'appPackage' : 'com.snailvr.manager',
    # 'appActivity' : 'com.whaley.vr.module.launcher.activitys.SplashActivity',
    'appActivity':"com.whaley.biz.launcher.activitys.MainActivity",
    'unicodeKeyborad' : True,
    'resetKeyborad' : True,
    'noReset' : True,
    'commandTimeout': 60,
    'autoGrantPermissions':True,
    "recreateChromeDriverSessions":True
    # 'automationName':'Uiautomator2'
}

remote_server = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(command_executor=remote_server,desired_capabilities=desired_caps)

driver.implicitly_wait(10)

# driver.find_element_by_id("com.snailvr.manager:id/iv_leapfrog").click()

driver.find_element_by_id(mybase).click()
driver.find_element_by_xpath(problemfeedback).click()

sleep(2)
context1 = driver.contexts
print context1
driver._switch_to.context("WEBVIEW_com.snailvr.manager")
cur = driver.current_context
print cur

ele = driver.find_element_by_class_name("description")

print ele.text

driver.find_element_by_id("q1").send_keys(u"测试测试")
driver.find_element_by_id('q2').send_keys(u"111111111")

driver.find_element_by_id("tqq3_7").send_keys(u"测试")
driver.find_element_by_id("tqq4_7").send_keys(u"测试")

sleep(1)
driver.find_element_by_id("ctlNext").click()

sleep(5)
ele = driver.find_element_by_class_name("description")
print ele.text
driver._switch_to.context("NATIVE_APP")
cur = driver.current_context
print cur
driver.find_element_by_id("com.snailvr.manager:id/titlebar_left").click()
sleep(4)
driver.quit()
