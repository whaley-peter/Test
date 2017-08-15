#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/14'
"""全局变量，多处通用"""
#by.id
#返回按钮
backbutton = "com.snailvr.manager:id/btn_back"

#标题栏
title = "com.snailvr.manager:id/tv_title"


from libs.launchManagerment import getProjectRootPath
apppath = getProjectRootPath()+ r"\app\WhaleyVR.apk"

desired_caps = {
    'platformName':'Android',
    'platformVersion' : '7.0',
    'deviceName' :'test',
    'udid':'GWY0217115007494',
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
username = '13764205429'
password = 'lang123456'

