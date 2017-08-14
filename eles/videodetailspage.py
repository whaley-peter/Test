#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/14'

from minepage import *

"""全景视频详情页"""

#视频名称
videoname = "com.snailvr.manager:id/tv_program_name"

#视频播放次数
videoplaycounts = "com.snailvr.manager:id/tv_play_count"

#加入播单
addtocollection = mycollection
collectiontext = "//*[@resource-id='com.snailvr.manager:id/layout_collect']//android.widget.TextView"

#缓存
downloadbutton = "com.snailvr.manager:id/layout_downlod"
downliadtext = "//*[@resource-id='com.snailvr.manager:id/layout_downlod']//android.widget.TextView"

#发布者名称
postername = "com.snailvr.manager:id/tv_poster_name"

#发布者粉丝数
posterfans = "com.snailvr.manager:id/tv_poster_fans"

#关注发布者
posterfollow = "com.snailvr.manager:id/tv_follow"
