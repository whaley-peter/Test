*** Settings ***
Library              libs/AppiumExtend.py
Variables            eles/homepage.py
Variables            eles/videodetailspage.py
Suite Setup          back to homepage
Suite Teardown       back to homepage
Force Tags           movie
Documentation        测试3D电影详情页

*** Test Cases ***
跳转到3D电影详情页--testmovie001
    detete all collection
    wait until element is visible            id=${homebase}                10
    click nth element until no error         id=${homebase}
    swipe left nth                           5
    wait until element is visible            xpath=${recommend_eles}       10
    swipe up nth
    ${moviename}                             get nth element text          id=${recommend_eles_name}
    click nth element until no error         xpath=${recommend_eles}
    ${moviename1}                            get text                      id=${videoname}
    should be equal     ${moviename}         ${moviename1}

判断视频详情信息--testmovie002
    element should contain text in time      id=${district_title}           地区
    element should contain text in time      id=${district}                 欧美
    element should contain text in time      id=${year_title}               年代
    element should contain text in time      id=${year}                     2011
    element should contain text in time      id=${director_title}           导演
    element should contain text in time      id=${director}                 西蒙·威尔斯
    element should contain text in time      id=${actor_title}              主演
    element should contain text in time      id=${actor}                    赛斯·格林;琼·库萨克;伊莉莎白·哈诺伊斯;丹·福勒
    element should contain text in time      id=${description}              在一个宁静的夜晚
    page should not contain element          id=${postername}
    page should not contain element          id=${posterfollow}

判断加入播单及缓存功能--testmovie003
    element should contain text in time      xpath=${downloadbuttontext}    缓存
    element should contain text in time      xpath=${collectiontext}        加入播单
    click element until no error             id=${downloadbutton}
    click element until no error             id=${addtocollection}
    element should contain text in time      xpath=${downloadbuttontext}    缓存
    element should contain text in time      xpath=${collectiontext}        已加入播单
    click nth element until no error         id=${addtocollection}
    element should contain text in time      xpath=${collectiontext}        加入播单

#分享功能--testqjspxqy003
#    element should contain text in time      xpath=${video_sharetext}       分享
#    share test                               3D火星救母记
