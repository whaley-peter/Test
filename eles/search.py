#!/usr/bin/env python
# -*- coding: utf-8 -*-
__mtime__ = '2017/8/21'
from homepage import homebase
"""home界面"""
#底部首页button
homepage = homebase
#home界面搜索
homepage_search = "com.snailvr.manager:id/view_search_bg"
#home界面搜索文字
homepage_search_text = "com.snailvr.manager:id/tv_search"


"""搜索界面"""
#搜索框
search_input = "com.snailvr.manager:id/et_search"
#搜索框文字提示
search_text = search_input
#搜索按钮
searchbutton = "com.snailvr.manager:id/tv_search"
searchbutton_text = searchbutton

#搜索为空图标
search_empty_pic = "com.snailvr.manager:id/iv_img"
#搜索为空字样
search_empty_text = "com.snailvr.manager:id/tv_empty"

#取消搜索
quxiao = searchbutton

#搜索到的视频
searched_video_pic = "com.snailvr.manager:id/pic"
#搜索到的视频名
searched_video_name = "com.snailvr.manager:id/name"


# 第一条搜索历史
history1 = "//*[@resource-id='com.snailvr.manager:id/rv_history']//android.widget.RelativeLayout[1]"

history_text = "//*[@resource-id='com.snailvr.manager:id/rv_history']//android.widget.RelativeLayout[1]//android.widget.TextView"

#清空搜索历史
search_history_delete= "com.snailvr.manager:id/layout_delete"
#清空字样
search_history_delete_text="com.snailvr.manager:id/tv_delete"

