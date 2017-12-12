#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sharepage import share_text,share
__mtime__ = '2017/8/14'




"""视频详情页名称、播放次数、下载、加入播单"""
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

#分享
video_share = share
video_share_text = share_text
#复制链接
video_share_copy = 'com.snailvr.manager:id/share_copy'
#×号
video_share_back_icon = 'com.snailvr.manager:id/back_icon'


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


"""发布者详情页"""
#发布者名称
publisher_name = "//*[@resource-id='com.snailvr.manager:id/rl_header']//android.widget.TextView[1]"
#发布者粉丝数
publisher_fans = "//*[@resource-id='com.snailvr.manager:id/rl_header']//android.widget.TextView[2]"
#发布者简介
publisher_info = "//*[@resource-id='com.snailvr.manager:id/rl_header']//android.widget.TextView[3]"
#关注发布者
publicist = 'com.snailvr.manager:id/btn_follow'



"""专题详情页"""
#专题名//专题内视频名
topic_name = 'com.snailvr.manager:id/tv_name'
#专题分享
topic_share = 'com.snailvr.manager:id/titlebar_right'
#专题视频个数
topic_video_num = 'com.snailvr.manager:id/tv_numVideo'
#专题简介
topic_decription = 'com.snailvr.manager:id/tv_summary'
#播放整个专题
topic_play = 'com.snailvr.manager:id/iv_player'
#专题内节目海报
videos_pic_topic = 'com.snailvr.manager:id/iv_pic'
#专题内节目名称
videos_name_in_topic = topic_name
#播放整个专题时,视频名称
video_name_in_topic_play = 'com.snailvr.manager:id/tv_title'

#上滑界面后，标题栏显示专题名称
topic_name_in_titlebar = "//*[@resource-id='com.snailvr.manager:id/titlebar_center']//android.widget.TextView"
#===============专题底部分享按钮================
#标题文案--分享专题至
topic_share_to_title = "com.snailvr.manager:id/tv_share"
#新浪
topic_share_sina = "//*[@resource-id='com.snailvr.manager:id/layout_sina']//android.widget.TextView"
#微信
topic_share_weixin = "//*[@resource-id='com.snailvr.manager:id/layout_wx']//android.widget.TextView"
#朋友圈
topic_share_weixinfriends = "//*[@resource-id='com.snailvr.manager:id/layout_wxfrends']//android.widget.TextView"
#qq好友
topic_share_qq = "//*[@resource-id='com.snailvr.manager:id/layout_qq']//android.widget.TextView"
#qq空间
topic_share_qqzone = "//*[@resource-id='com.snailvr.manager:id/layout_qzone']//android.widget.TextView"


"""直播预告详情页"""
#直播tab
live = 'com.snailvr.manager:id/tv_live'
#直播预告tab
liveprevue_page = "//*[@resource-id='com.snailvr.manager:id/title_container']//android.view.View[2]"
#直播预告tab，节目名称
name_in_liveprevue_page = 'com.snailvr.manager:id/tv_name'
#直播预告tab，节目简介
description_in_liveprevue_page  = 'com.snailvr.manager:id/tv_content'
#直播预告tab，预约、取消预约
add_in_liveprevue_page  = 'com.snailvr.manager:id/tv_add'
#================直播预约详情页============================
#直播预告名称
liveprevue_name = 'com.snailvr.manager:id/tv_title'
#直播预告分享
liveprevue_share = 'com.snailvr.manager:id/btn_share'
#已预约人数
liveprevue_people = 'com.snailvr.manager:id/tv_people'
liveprevue_people_account = 'com.snailvr.manager:id/tv_amount'
#直播预告预约、取消预约按钮
liveprevue_add = 'com.snailvr.manager:id/btn_reserve'
#距离开播时间
liveprevue_date = 'com.snailvr.manager:id/tv_date'#距离2017.12.31 23:55 开播还有
liveprevue_date_remain = 'com.snailvr.manager:id/tv_remain'#天数，例如19
liveprevue_date_unit = 'com.snailvr.manager:id/tv_unit'#单位，天
#直播地址
liveprevue_location = 'com.snailvr.manager:id/tv_location'
#直播预告简介
liveprevue_description = 'com.snailvr.manager:id/tv_intro'

"""节目包详情页"""
#banner上节目名称

#节目包价格显示
package_price = 'com.snailvr.manager:id/tv_buy' #购买节目包观看券 ¥0.05




