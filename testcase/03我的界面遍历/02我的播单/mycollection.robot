*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Variables   eles/loginpage.py

*** Test Cases ***
清空我的播单--testwodebodan001
    click element       id=${mybase}
    click element       xpath=${mycollection}
    delete all element
    back to homepage

加入我的播单--testwodebodan002
    [Documentation]  加入播单并检查播单
#加入第一个视频
    click element   id=${homepage}
    click element   xpath=${zongyi}
    wait until element is visible   xpath=${video1}     10
    click element   xpath=${video1}
    ${tvdes1}       get text        id=${programname}
    wait until element is visible       id=${collectbodan}      5
    click element   id=${collectbodan}
    sleep   3
    ${text}      get text     xpath=${collecttext1}
    should be equal        ${text}       已加入播单
    click back nth
#加入第二个视频
    wait until element is visible   xpath=${video2}     10
    click element   xpath=${video2}
    wait until element is visible       id=${collectbodan}      5
    click element   id=${collectbodan}
    sleep   3
    ${text}      get text     xpath=${collecttext1}
    should be equal        ${text}       已加入播单
    click back nth
#加入第三个视频
    wait until element is visible   xpath=${video3}     10
    click element   xpath=${video3}
    wait until element is visible       id=${collectbodan}      5
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

删除播单操作--testwodebodan003
    [Documentation]  取消删除和删除操作

#取消删除播单
    page should contain element     id=${bianji}
    click element       id=${bianji}
    element should contain text  id=${clickall}     全选
    element should contain text  id=${delete}       删除
    click nth element      id=${click}      1
    click element      id=${delete}
    page should contain element     id=${content}
    click element      id=${quxiao}
    click element      id=${clickall}
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

退出登录从我的播单登录--testwodebodan004
    [Documentation]  退出登录并通过我的播单登录
#退出登录
    logout
#从我的播单登录
    wait until element is visible       xpath=${mycollection}       10
    click element       xpath=${mycollection}
    page should contain element         id=${content}
    click element       id=${confirm}
    input text      id=${usernameinput}     ${username}
    input text      id=${passwordinput}     ${password}
    click element   id=${loginbutton}
    element should contain text         xpath=${title}          我的播单