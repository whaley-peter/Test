*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/homepage.py
Variables           eles/videodetailspage.py
Suite Setup         back to homepage
Suite Teardown      swipe nth back to jingxuan tab      3
#Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     qjspxqy
Force Tags          qjspxqy

*** Test Cases ***
清空我的播单、发布者、缓存--testqjspxqy001
    detete all collection
    delete all download
    delete all attented publishers

跳转到视频详情页--testqjspxqy002
    back to homepage
    wait until element is visible            id=${homebase}                 10
    click element until no error             id=${homebase}
    swipe left nth      3
    sleep               2
    click nth element until no error         xpath=${recommend_eles}        2

判断视频名称及播放次数--testqjspxqy003
    element should contain text in time      id=${videoname}                JHH视频2（勿动!!!）
    element should contain text in time      id=${videoplaycounts}          次播放

判断加入播单及缓存功能--testqjspxqy004
    element should contain text in time      xpath=${downloadbuttontext}    缓存
    element should contain text in time      xpath=${collectiontext}        加入播单
    click element until no error             id=${downloadbutton}
    click element until no error             id=${addtocollection}
    element should contain text in time      xpath=${downloadbuttontext}    已缓存
    element should contain text in time      xpath=${collectiontext}        已加入播单

判断关注及跳转发布者详情页--testqjspxqy005
    page should not contain element          id=${description}
    ${name}     get text                     id=${postername}
    element should contain text in time      id=${posterfollow}             关注
    click element until no error             id=${posterfollow}
    element should contain text in time      id=${posterfollow}             已关注
    click element until no error             id=${postername}
    wait until element is visible            xpath=${publisher name}        5
    ${name1}    get text                     xpath=${publisher name}
    should be equal     ${name}              ${name1}
    element should contain text in time      xpath=${publisher fans}        粉丝
    element should contain text in time      id=${publicist}                已关注
    click element until no error             id=${publicist}
    click back nth
    element should contain text in time      id=${posterfollow}             关注

#分享功能--testqjspxqy006
#    element should contain text in time      xpath=${video_sharetext}       分享
#    share test                               自动化测试--gzh免费节目001