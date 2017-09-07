*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Variables   eles/loginpage.py

*** Test Cases ***
加入我的播单--testwodebodan001
    [Documentation]  加入播单并检查播单
#加入第一个视频
    click element   id=${homepage}
    click element   xpath=${zongyi}
    wait until element is visible   xpath=${video1}     10
    click element   xpath=${video1}
    ${tvdes1}       get text        id=${programname}

    click element   id=${collectbodan}
    sleep   3
    ${text}      get text     xpath=${collecttext1}
    should be equal        ${text}       已加入播单
    click back nth
#加入第二个视频
    wait until element is visible   xpath=${video2}     10
    click element   xpath=${video2}
    click element   id=${collectbodan}
    sleep   3
    ${text}      get text     xpath=${collecttext1}
    should be equal        ${text}       已加入播单
    click back nth
#加入第三个视频
    wait until element is visible   xpath=${video3}     10
    click element   xpath=${video3}
    click element   id=${collectbodan}
    sleep   3
    ${text}      get text     xpath=${collecttext1}
    should be equal        ${text}       已加入播单
    click back nth

#进入检查我的播单
    click element       id=${mybase}
    click element       xpath=${mycollection}
    element should contain text     xpath=${title}      我的播单
    ${boname1}       get nth element text    id=${bodanname}   -1
    should be equal     ${tvdes1}       ${boname1}
删除播单操作--testwodebodan002
    [Documentation]  取消删除和删除操作

#取消删除播单
    page should contain element     id=${bianji}
    click element       id=${bianji}
    page should contain element     id=${layout_check}
    click nth element      id=${check}      1
    click element      id=${delete}
    page should contain element     id=${content}
    click element      id=${quxiao}
    click element      id=${checkall}
    is all selected
    click element      id=${rightquxiao}

#删除一个播单
    page should contain element     id=${bianji}
    ${videonamea}      get nth element text     id=${videoname}      1
    delete nth element      1
    ${videonameb}      get nth element text     id=${videoname}      1
    should not be equal     ${videonamea}       ${videonameb}

#删除所有播单
    page should contain element     id=${bianji}
    delete all element
    Page Should Not Contain Element     id=${bodanvideo}
    element should contain text         id=${mycollectionempty}         暂无视频加入播单
    click back nth
退出登录从我的播单登录--testwodebodan003
    [Documentation]  退出登录并通过我的播单登录
#退出登录
    wait until element is visible       id=${settingbutton}         10
    click element       id=${settingbutton}
    element should contain text         xpath=${title}         设置
    page should contain element         id=${logoutbutton}
    click element       id=${logoutbutton}
    page should contain element         id=${content}
    click element       id=${confirm}
    page should contain element         id=${notlogin}
#从我的播单登录
    wait until element is visible       xpath=${mycollection}       10
    click element       xpath=${mycollection}
    page should contain element         id=${content}
    click element       id=${confirm}
    element should contain text         xpath=${title}         登录
    input text          id=${usernameinput}         18616512272
    input text          id=${passwordinput}         a123456
    click element       id=${loginbutton}
    page should contain element         xpath=${title}
    element should contain text         xpath=${title}          我的播单




