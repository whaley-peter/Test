*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/minepage.py
Variables           eles/globaleles.py
Variables           eles/loginpage.py
Suite Setup         back to homepage
Suite Teardown      swipe nth back to jingxuan tab      3
Test Setup          kill logcat         ${udid}
Test Teardown       run keyword if test failed       logcat     ${udid}     wodebodan
Force Tags          wodebodan

*** Test Cases ***
清空我的播单--testwodebodan001
    click element until no error     id=${mybase}
    click element until no error     xpath=${mycollection}
    delete all element
    back to homepage
加入我的播单--testwodebodan002
    [Documentation]  加入播单并检查播单
#加入第一个视频
    click element until no error            id=${homepage}
    swipe right nth                         3
    click element until no error            xpath=${zongyi}
    wait until element is visible           xpath=${video1}         10
    click element until no error            xpath=${video1}
    ${tvdes1}       get text                id=${programname}
    wait until element is visible           id=${collectbodan}      5
    click element until no error            id=${collectbodan}
    element should contain text in time     xpath=${collecttext1}   已加入播单
    click back nth
#加入第二个视频
    wait until element is visible           xpath=${video2}         10
    click element until no error            xpath=${video2}
    wait until element is visible           id=${collectbodan}      5
    click element until no error            id=${collectbodan}
    element should contain text in time     xpath=${collecttext1}   已加入播单
    click back nth
#加入第三个视频
    wait until element is visible           xpath=${video3}         10
    click element until no error            xpath=${video3}
    wait until element is visible           id=${collectbodan}      5
    click element until no error            id=${collectbodan}
    element should contain text in time     xpath=${collecttext1}   已加入播单
    click back nth
#进入检查我的播单
    click element until no error             id=${mybase}
    click element until no error             xpath=${mycollection}
    wait until element is visible            xpath=${title}         5
    element should contain text in time      xpath=${title}         我的播单
    ${boname1}       get nth element text    id=${bodanname}        -1
    should be equal     ${tvdes1}            ${boname1}

删除播单操作--testwodebodan003
    [Documentation]  取消删除和删除操作
#取消删除播单
    click element until no error                    id=${bianji}
    element should contain text in time             id=${clickall}     全选
    element should contain text in time             id=${delete}       删除
    click nth element                               id=${click}        1
    click element until no error                    id=${delete}
    page should contain element                     id=${content}
    click element until no error                    id=${quxiao}
    click back nth                                  2
    click element until no error                    xpath=${mycollection}
#删除一个播单
    element should contain text in time             xpath=${bianjitext}     编辑
    ${videonamea}      get nth element text         id=${videoname}     1
    delete nth element
    click back nth
    click element until no error                    xpath=${mycollection}
    nth element should not contain text in time     id=${videoname}     ${videonamea}
#删除所有播单
    delete all element
    click back nth
    click element until no error                    xpath=${mycollection}
    element should contain text in time             id=${mycollectionempty}         暂无视频加入播单
    click back nth

#退出登录从我的播单登录--testwodebodan004
#    [Documentation]  退出登录并通过我的播单登录
##退出登录
#    logout
##从我的播单登录
#    wait until element is visible    xpath=${mycollection}       10
#    click element until no error     xpath=${mycollection}
#    page should contain element      id=${content}
#    click element until no error     id=${confirm}
#    input text                       id=${usernameinput}     ${username}
#    input text                       id=${passwordinput}     ${password}
#    click element until no error     id=${loginbutton}
#    wait until element is visible    xpath=${title}          5
#    element should contain text in time         xpath=${title}          我的播单



