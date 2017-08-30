#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/10'
#底部首页button
homepage = "com.snailvr.manager:id/rl_recommend"
#tab 综艺
zongyi = "//android.widget.LinearLayout/android.view.View[4]"

#我 tap button
mybase = "com.snailvr.manager:id/tv_user" #id

"""个人信息"""
#用户名
nickname = "com.snailvr.manager:id/tv_nick_name" #id


"""设置界面及二级目录"""
#设置按钮
settingbutton = "com.snailvr.manager:id/iv_setting" #id

#清除缓存
setting_clean_cache = "//android.support.v7.widget.RecyclerView//android.widget.FrameLayout[2]"  #xpath

#切换到debug模式
debugswitch = "//android.support.v7.widget.RecyclerView//android.widget.FrameLayout[6]//android.widget.TextView[1]" #xpath

#退出登录
logoutbutton = "com.snailvr.manager:id/btn_logout" #id


"""本地界面及二级目录"""
#本地管理
localmanagement = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[1]" #xpath
#离线缓存\本地视频
offlinecache = "android.support.v7.app.ActionBar$Tab"   #class
#视频名
tvname = "com.snailvr.manager:id/tv_name"
#编辑
bianji = "com.snailvr.manager:id/titlebar_right"
#右上角取消
rightquxiao = bianji
#选择
check = "com.snailvr.manager:id/iv_check"
#全选
checkall = "com.snailvr.manager:id/cb_check_all"
#删除
delete = "com.snailvr.manager:id/btn_delete"
#继续
confirm = "com.snailvr.manager:id/tv_confirm"
#取消
quxiao = "com.snailvr.manager:id/tv_cancel"
#本地视频或者离线缓存为空
localempty = "com.snailvr.manager:id/tv_empty"


#相册视频导入
xiangce = "com.snailvr.manager:id/btn_gallery"
#相册中视频
layout = "com.snailvr.manager:id/pic_layout"
#相册中视频名
layname = "com.snailvr.manager:id/name"
#导入
daoru = "com.snailvr.manager:id/btn_import"
#确定
ok = "com.snailvr.manager:id/tv_ok"
#视频名
videoname = "com.snailvr.manager:id/name"

#链接导入
link = "com.snailvr.manager:id/btn_link"
#链接导入框
suggestion ="com.snailvr.manager:id/suggestion"

#二维码导入
qrcode = "com.snailvr.manager:id/btn_qrcode"


"""我的播单界面及二级目录"""
#我的播单
mycollection = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[2]" #xpath
#我的播单为空
mycollectionempty = "com.snailvr.manager:id/tv_error"
#播单中视频
bodanvideo ="com.snailvr.manager:id/pic"
#播单中视频名
bodanname = "com.snailvr.manager:id/name"


"""我的券/兑换码及二级目录"""
#我的券/兑换码
mycoupen = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[3]" #xpath
#兑换码输入框
mabox = "com.snailvr.manager:id/rl_redemption_box"
#请输入兑换码字样
maname = "//*[@resource-id='com.snailvr.manager:id/rl_redemption_box']//android.widget.TextView"
#观看券中视频名
quanname = "com.snailvr.manager:id/tv_name"
#明细
mingxi = "com.snailvr.manager:id/btn_right"
#上方标题标题
title = "com.snailvr.manager:id/tv_title"
#明细中说明
paynum="com.snailvr.manager:id/tv_pay_num"


"""我的奖品及二级目录"""
#我的奖品
mygift = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[4]"
#右上添加按钮
address = "com.snailvr.manager:id/btn_address"
#收货人
etname = "com.snailvr.manager:id/et_name"
#联系电话
etnumber = "com.snailvr.manager:id/et_number"
#所在地址
etaddress = "com.snailvr.manager:id/et_address"
#上海长宁区城区
shanghai = "//android.widget.ListView/android.widget.RelativeLayout[2]"
changning = "//android.widget.ListView/android.widget.RelativeLayout[3]"
chengqu = "//android.widget.ListView/android.widget.RelativeLayout"
#详细地址
fulladdress = "com.snailvr.manager:id/et_full_address"
#提交
submit = "com.snailvr.manager:id/bin_submit"

"""问题反馈及二级目录"""
#问题反馈
problemfeedback = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[5]"  #xpath


#官方论坛
forum = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[6]" #xpath

"""使用帮助及二级目录"""
#使用帮助
usehelp = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[7]" #xpath

"""关于及二级目录"""
#关于
about = "//*[@resource-id='com.snailvr.manager:id/me_layout']//android.widget.FrameLayout[8]" #xpath
#图标
icon = "com.snailvr.manager:id/iv_icon"
#加入QQ群
enter = "com.snailvr.manager:id/tv_enter_qq"
#商务合作
trade = "com.snailvr.manager:id/tv_trade"
#用户协议
agreement="com.snailvr.manager:id/user_agreement"

"""选择缓存视频"""
#综艺频道左下视频
video1 ="//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]"
#综艺频道右下视频
video2 ="//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]"
#半屏详情页视频名
programname = "com.snailvr.manager:id/tv_program_name"
#缓存
download = "com.snailvr.manager:id/layout_downlod"
#已缓存字样
downloadtext1 = "//*[@resource-id='com.snailvr.manager:id/layout_downlod']//android.widget.TextView"

"""将视频加入播单"""
# 加入播单s
collectbodan="com.snailvr.manager:id/layout_collect"



