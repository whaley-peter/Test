#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/10'

"""登录home界面"""
#by.id
#登录按钮
loginbutton = "com.snailvr.manager:id/btn_login"

#注册按钮
registerbutton = "com.snailvr.manager:id/btn_register"

#先逛一逛
leapfrog = "com.snailvr.manager:id/iv_leapfrog"


"""登录主界面"""
#by.id
#输入账号框//------注册界面输入手机号框
usernameinput = "com.snailvr.manager:id/et_input"
usernameinput_text = "//*[@resource-id='com.snailvr.manager:id/et_user_name']//com.snailvr.manager:id/et_user_name"
#输入密码框
passwordinput = "com.snailvr.manager:id/et_password"

#短信快捷登录
safe_login = "com.snailvr.manager:id/btn_safe_login"

#短信快捷登录
forget_pwd = "com.snailvr.manager:id/btn_forget_pwd"

#找回密码界面
connect_us = "com.snailvr.manager:id/tv_connect_us"

#跳转到注册界面按钮//-------注册界面跳转到登录界面按钮
jump_to_login_or_register = "com.snailvr.manager:id/titlebar_right"
jump_to_login_or_register_text = "//*[@resource-id='com.snailvr.manager:id/titlebar_right']//android.widget.TextView"

"""注册主界面"""
#注册输入名称
registerinput = "com.snailvr.manager:id/et_phone"
registerinput_text = "//*[@resource-id='com.snailvr.manager:id/et_phone']//android.widget.EditText"

#输入验证码框
msm_code_input = "com.snailvr.manager:id/layout_sms_code"
#输入安全码提示语
msm_code_input_text = "//*[@resource-id='com.snailvr.manager:id/et_sms_code']//android.widget.EditText"
#获取安全码提示语
msm_code_get = "com.snailvr.manager:id/btn_fetch_code"

#点击下一步
next_step = "com.snailvr.manager:id/btn_next"

#=========第三方登录、注册==========================================
#使用第三方app登录或者注册提示语
third_app_title = "com.snailvr.manager:id/tv_third_title"

#跳转到qq
start_qq = 'com.snailvr.manager:id/start_qq'
#qq登录界面title
qq_title = 'com.tencent.mobileqq:id/ivTitleName'
#qq界面授权登录按钮
login_by_qq = '//android.widget.Button'  #xpath
#qq登录界面返回按钮
back_from_qq_login = "com.tencent.mobileqq:id/ivTitleBtnLeft"

#跳转到微信
start_weixin = "com.snailvr.manager:id/start_weixin"
#微信登录界面title
weixin_title = 'android:id/text1'
#微信界面确认登录按钮
login_by_weixin = 'btnOk'  #H5网页元素
#微信登录界面返回按钮
back_from_weixin_login = 'com.tencent.mm:id/h4'


#跳转到微博
start_weibo = 'com.snailvr.manager:id/start_weibo'
#微博登录界面title
title_of_weibo = "com.sina.weibo:id/titleText"
#微博界面授权登录按钮
login_by_weibo = "com.sina.weibo:id/bnLogin"
#微博登录界面返回按钮
back_from_weibo_login = "com.sina.weibo:id/titleBack"

#找回密码界面-联系我们
connect_us = 'com.snailvr.manager:id/tv_connect_us'

