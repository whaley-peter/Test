*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/myattentionpage.py
Variables           eles/videodetailspage.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     fabuzhe
Force Tags          fabuzhe

*** Test Cases ***
跳转到我的关注并清空关注的发布者---testfabuzhe001
    wait until element is visible       id=${myattention}       10
    delete all attented publishers

从推荐关注界面跳转到发布者详情页---testfabuzhe002
    click element until no error        id=${suggested attention}
    ${val}  get nth element text        id=${publishers_name}
    click nth element until no error    id=${publishers_pic}
    ${val1}             get text        xpath=${publisher name}
    should be equal     ${val}          ${val1}

发布者详情页---testfabuzhe003
    click nth element until no error        id=${publicist}
    element should contain text in time     id=${publicist}                 已关注
    element should contain text in time     xpath=${publisher fans}         粉丝
    ${name}                                 get text                        xpath=${publisher name}
    ${ju}            should be equal        ${name}        微鲸VR
    run keyword if   ${ju}        element should contain text in time     xpath=${publisher info}     事实上是是是
    click back nth   2