*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/homepage.py
Variables   eles/videodetailspage.py
#Suite Setup     back to homepage
#Suite Teardown      back to homepage
Force Tags      qjspxqy
Documentation   测试全景视频详情页功能，下载、加入播单、关注发布者、跳转到发布者详情页

*** Test Cases ***
跳转到全景视频详情页--testqjspxqy001
    wait until element is visible       id=${homebase}
    swipe left nth   1
    sleep       3
    click nth element until no error    xpath=${video}        3
    sleep  2
判断视频名称
    element should contain text in time     id=${videoname}              自动化测试--gzh免费节目001
##判断播放次数
#    element should contain text in time     xpath=${videoplaycounts}        次播放
##判断加入播单及缓存功能
#    element should contain text in time      xpath=${downloadbuttontext}    缓存
#    element should contain text in time      xpath=${collectiontext}        加入播单
#    click element until no error             id=${downloadbutton}
#    click element until no error             id=${addtocollection}
#    element should contain text in time      xpath=${downloadbuttontext}    已缓存
#    element should contain text in time      xpath=${collectiontext}        已加入播单
分享功能
#    element should contain text in time      xpath=${sharetext}             分享

     share test         自动化测试--gzh免费节目001
##判断关注及跳转发布者详情页
#    page should contain element              id=${share}
#    page should not contain element          id=${description}
#    element should contain text in time      id=${postername}           微鲸VR
#    element should contain text in time      id=${posterfollow}         关注
     click element until no error             id=${posterfollow}         已关注

