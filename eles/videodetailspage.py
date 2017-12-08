#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/14'

"""全景视频详情页"""

#视频名称
videoname = "com.snailvr.manager:id/tv_program_name"

#视频播放次数
videoplaycounts = "com.snailvr.manager:id/tv_play_count"

#加入播单
addtocollection = "com.snailvr.manager:id/layout_collect"
collectiontext = "//*[@resource-id='com.snailvr.manager:id/layout_collect']//android.widget.TextView"

#缓存
downloadbutton = "com.snailvr.manager:id/layout_downlod"
downloadbuttontext = "//*[@resource-id='com.snailvr.manager:id/layout_downlod']//android.widget.TextView"

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
share_text_of_qq_zone = "//android.widget.TextView[3]"
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


#复制链接
share_copy = 'com.snailvr.manager:id/share_copy'
#×号
share_back_icon = 'com.snailvr.manager:id/back_icon'



"""视频详情页发布者模块"""
#发布者名称
postername = "com.snailvr.manager:id/tv_poster_name"
#发布者粉丝数
posterfans = "com.snailvr.manager:id/tv_poster_fans"
#关注发布者
posterfollow = "com.snailvr.manager:id/tv_follow"




"""3D电影详情页"""
#评分
pingfen = "com.snailvr.manager:id/tv_rate"

#地区
district_title = 'com.snailvr.manager:id/tv_district_title'
district = 'com.snailvr.manager:id/tv_district'

#年代
year_title = 'com.snailvr.manager:id/tv_year_title'
year = 'com.snailvr.manager:id/tv_year'

#导演
director_title = 'com.snailvr.manager:id/tv_director_title'
director = 'com.snailvr.manager:id/tv_director'

#主演
actor_title = 'com.snailvr.manager:id/tv_actor_title'
actor = 'com.snailvr.manager:id/tv_actor'

#简介
description = 'com.snailvr.manager:id/tv_description'

#返回
back = "com.snailvr.manager:id/btn_back"

"""互动剧详情页"""
#切换分支剧情海报图-左侧
switch_branch_left = 'com.snailvr.manager:id/iv_left'
#切换分支剧情海报图-中间
switch_branch_middle = 'com.snailvr.manager:id/iv_middle'
#切换分支剧情海报图-右侧
switch_branch_right = 'com.snailvr.manager:id/iv_right'




#即将播放
loadingtext = "com.snailvr.manager:id/tv_loading_text"

#自动化测试tab页
testtab = "//android.widget.RelativeLayout//android.widget.HorizontalScrollView//android.view.View[2]"


#新歌声推荐位
video = "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout"