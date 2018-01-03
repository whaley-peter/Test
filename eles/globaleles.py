#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
"""全局变量，多处通用"""
#by.id
#返回按钮
backbutton = "com.snailvr.manager:id/titlebar_left"

#标题栏
title = "//*[@resource-id='com.snailvr.manager:id/titlebar_center']//android.widget.TextView"

#弹框上取消按钮
canclebutton = "com.snailvr.manager:id/tv_cancel"

#弹框上确定按钮
confirmbutton = "com.snailvr.manager:id/tv_confirm"

def getProjectRootPath():
    """get rootpath of project
    """
    rootpath = os.getcwd().split('\eles')[0]
    return rootpath

apppath = getProjectRootPath()+ r"\app\launcher-debug.apk"

desired_caps = {
    'platformName':'Android',
    'platformVersion' : '7.0',
    'deviceName' :'test',
    # 'udid':'5e321b32',
    'app' : apppath,
    'appPackage' : 'com.snailvr.manager',
    'appActivity':'com.whaley.biz.launcher.activitys.LauncherActivity',
    'unicodeKeyboard' : True,
    'resetKeyboard' : True,
    'noReset' : True,
    'commandTimeout': 60,
    'autoGrantPermissions':True,
    'sessonOverride': True,
    # 'automationName': 'Uiautomator2'

}

remote_server = 'http://localhost:4723/wd/hub'

username = '18616512272'
password = 'a123456'
usernickname = "ABCD"

username1 = '13764205429'
password1 = 'lang123456'
usernickname1 = '浪'

username3 = '13636423651'
password3 = 'a123456'
usernickname3 = '5451'



if __name__=="__main__":
    print getProjectRootPath()