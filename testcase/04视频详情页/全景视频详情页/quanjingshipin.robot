*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/homepage.py
Variables   eles/videodetailspage.py
Documentation   测试全景视频详情页功能，下载、加入播单、关注发布者、跳转到发布者详情页

*** Test Cases ***
跳转到全景视频详情页
    wait until element is visible       id=${homebase}
    swipe left nth   1
    swipe up nth    1
    click nth element until no error    id=com.snailvr.manager:id/tv_des        3
    sleep  2
    click element until no error    id=${add to collection}
    element should contain text     xpath=${collectiontext}     已加入播单
    sleep  2
