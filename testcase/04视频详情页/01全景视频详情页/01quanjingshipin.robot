*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/homepage.py
Variables           eles/videodetailspage.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
Force Tags          qjspxqy

*** Test Cases ***
跳转到全景视频详情页--testqjspxqy001
    detete all collection
    detete all download
    delete all attented publishers
    wait until element is visible            id=${homebase}                 10
    click element until no error             id=${homebase}
    swipe left nth      1
    click nth element until no error         xpath=${recommend_eles}        3
    sleep               2

判断视频名称及播放次数--testqjspxqy002
    element should contain text in time      id=${videoname}                自动化测试--gzh免费节目001
    element should contain text in time      id=${videoplaycounts}          次播放

判断加入播单及缓存功能--testqjspxqy003
    element should contain text in time      xpath=${downloadbuttontext}    缓存
    element should contain text in time      xpath=${collectiontext}        加入播单
    click element until no error             id=${downloadbutton}
    click element until no error             id=${addtocollection}
    element should contain text in time      xpath=${downloadbuttontext}    已缓存
    element should contain text in time      xpath=${collectiontext}        已加入播单

判断关注及跳转发布者详情页--testqjspxqy005
    page should not contain element          id=${description}
    element should contain text in time      id=${postername}               微鲸VR
    element should contain text in time      id=${posterfollow}             关注
    click element until no error             id=${posterfollow}
    element should contain text in time      id=${posterfollow}             已关注
    click element until no error             id=${postername}
    element should contain text in time      xpath=${publisher name}        微鲸VR
    element should contain text in time      xpath=${publisher fans}        粉丝
    element should contain text in time      id=${publicist}                已关注
    click element until no error             id=${publicist}
    click back nth
    element should contain text in time      id=${posterfollow}             关注

#分享功能--testqjspxqy004
#    element should contain text in time      xpath=${video_sharetext}       分享
#    share test                               自动化测试--gzh免费节目001