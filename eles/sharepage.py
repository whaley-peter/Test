#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/12/11'
"""分享模块"""
#分享
share = "com.snailvr.manager:id/layout_share"
share_text = "//*[@resource-id='com.snailvr.manager:id/layout_share']//android.widget.TextView"
#========================================调出分享框======================================#
#新浪微博
sina_weibo = 'com.snailvr.manager:id/sina_weibo'
#---微博界面---分享成功后自动回到app
#取消分享
cancle_weibo_share = 'com.sina.weibo:id/titleBack'
#发送分享
share_to_weibo = 'com.sina.weibo:id/titleSave'
#分享文案
share_text_of_weibo = 'com.sina.weibo:id/edit_view'


#微信好友
weixin_friend = 'com.snailvr.manager:id/weixin_friend'
#---微信好友界面---分享成功后点击回到微鲸VR，回到app
#好友列表第一个好友
first_weixin_friend = '//android.widget.ListView//android.widget.RelativeLayout[2]'
#分享文案
share_text_of_weixin_friend = 'com.tencent.mm:id/adc'
#分享到微信好友
share_to_weixin_friend = 'com.tencent.mm:id/ad8'
#分享成功后，点击返回回到微鲸VR
back_to_whaley_from_weixin_friends = 'com.tencent.mm:id/ad7'
#取消分享
cancle_weixin_friend_share = 'com.tencent.mm:id/h4'

#朋友圈
weixin_circle = 'com.snailvr.manager:id/weixin_circle'
#---微信朋友圈界面---分享成功后自动回到app
#分享文案
share_text_of_weixin_circle = 'com.tencent.mm:id/crg'
#分享到微信朋友圈
share_to_weixin_circle = 'com.tencent.mm:id/gl'
#取消分享
cancle_weixin_circle_share = cancle_weixin_friend_share


#QQ空间
qq_zone = 'com.snailvr.manager:id/qq_zone'
#---qq控件界面---分享成功后自动回到app
# 分享到qq空间
share_to_zone = 'com.tencent.mobileqq:id/ivTitleBtnRightText'
#分享文案
share_text_of_qq_zone = "//android.widget.ScrollView//android.widget.FrameLayout//android.widget.LinearLayout//android.widget.TextView"

#取消分享
cancle_qq_zone_share = 'com.tencent.mobileqq:id/ivTitleBtnLeftButton'


#QQ好友
qq_friend = 'com.snailvr.manager:id/qq_friend'
#---qq控件界面---分享成功后点击返回回到app
#好友列表第一个
first_qq_friend = '//android.widget.AbsListView//android.widget.RelativeLayout[2]'
#分享到qq好友
share_to_qq = 'com.tencent.mobileqq:id/dialogRightBtn'
share_text_of_qq_friend1 = "//android.widget.TextView[1]"
#分享文案
share_text_of_qq_friend = "//android.widget.FrameLayout//android.widget.LinearLayout[1]//android.widget.TextView"
#分享成功后，点击返回回到app
back_to_whaley_from_qq_friend = 'com.tencent.mobileqq:id/dialogLeftBtn'
#取消分享
cancle_qq_friend_share = 'com.tencent.mobileqq:id/ivTitleBtnRightText'


