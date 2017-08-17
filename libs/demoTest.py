#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/9'

from appium import webdriver
from time import sleep
import subprocess

desired_caps = {
    'platformName':'Android',
    'platformVersion' : '6.0.1',
    'deviceName' :'test',
    'udid':'8d5cd6c0',
    'app' : r'E:\Test\app\WhaleyVR.apk',
    'appPackage' : 'com.snailvr.manager',
    'appActivity' : 'com.whaley.vr.module.launcher.activitys.SplashActivity',
    'unicodeKeyborad' : True,
    'resetKeyborad' : True,
    'noRest' : True,
    'commandTimeout': 60,
    'autoGrantPermissions':True
}

remote_server = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(command_executor=remote_server,desired_capabilities=desired_caps)

# driver.find_element_by_id("com.snailvr.manager:id/btn_login").click()
# driver.find_element_by_id("com.snailvr.manager:id/et_user_name").send_keys("18616512272")
# driver.find_element_by_id("com.snailvr.manager:id/et_password").send_keys("a123456")
# driver.find_element_by_id("com.snailvr.manager:id/btn_login").click()
# sleep(10)

driver.find_element_by_id("com.snailvr.manager:id/tv_user").click()

driver.find_element_by_id("com.snailvr.manager:id/iv_setting").click()

driver.find_element_by_id("com.snailvr.manager:id/layout_debug").click()
driver.back()
driver.back()
cmd = "adb shell am start -n com.snailvr.manager/com.whaley.vr.module.launcher.activitys.SplashActivity"
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



driver.swipe()
