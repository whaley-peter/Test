#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""全局变量，多处通用"""
#by.id
#返回按钮
backbutton = "com.snailvr.manager:id/btn_back"

#标题栏
title = "com.snailvr.manager:id/tv_title"

#弹框上取消按钮
canclebutton = "com.snailvr.manager:id/tv_cancel"

#弹框上确定按钮
confirmbutton = "com.snailvr.manager:id/tv_confirm"


from libs.launchManagerment import getProjectRootPath
apppath = getProjectRootPath()+ r"\app\WhaleyVR.apk"

desired_caps = {
    'platformName':'Android',
    'platformVersion' : '6.0',
    'deviceName' :'test',
    'udid':'6221231716B0904714',
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

remote_server = 'http://localhost:4723/wd/hub'
username = '18616512272'
password = 'a123456'
usernickname = "ABCD"

username1 = '13764205429'
password1 = 'lang123456'
usernickname1 = 'lang'

username3 = '13636423651'
password3 = 'a123456'
usernickname3 = '5451'



