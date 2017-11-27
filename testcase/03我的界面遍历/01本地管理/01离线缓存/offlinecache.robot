*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/videodetailspage.py
Variables   eles/globaleles.py
*** Test Cases ***
选择视频进行缓存-testlocalcache001
    [Documentation]  选择视频进行缓存后进入本地管理-离线缓存检查视频
    click element   id=${homepage}
    click element   xpath=${zongyi}
#缓存第一个视频
    wait until element is visible   xpath=${video1}
    click element   xpath=${video1}
    ${tvdes1}       get text        id=${programname}
    click element   id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text     xpath=${downloadtext1}
    should be equal        ${val}       已缓存
#缓存第二个视频
    click back nth
    wait until element is visible   xpath=${video2}
    click element   xpath=${video2}
    click element   id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text     xpath=${downloadtext1}
    wait until element is visible   xpath=${downloadtext1}
    should be equal        ${val}       已缓存
#缓存第三个视频
    click back nth
    wait until element is visible   xpath=${video3}
    click element   xpath=${video3}
    click element   id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text     xpath=${downloadtext1}
    wait until element is visible   xpath=${downloadtext1}      10
    should be equal        ${val}       已缓存
检查离线缓存
    click back nth
    swipe right nth     3
#    click element until no error    xpath=${jingxuan}
    click element     id=${mybase}
    ${a}   get text     xpath=${tvtext}
    log to console      ${a}
    element should contain text     xpath=${tvtext}        万能VR播放器
    click element     xpath=${localmanagement}
    ${tvname1}       get nth element text    id=${tvname}   -1
#    should be equal     ${tvdes1}       ${tvname1}

取消和删除离线缓存-testlocalcache002
    [Documentation]  对离线缓存进行删除一个或多个的操作
#缓存中对视频操作
#    click nth element       id=${btndownload}       1
#    element should contain text     id=${btndownload}       继续
#    click nth element       id=${btndownload}       1
#编辑——选中一个视频
    ${tvnamea}       get nth element text    id=${tvname}   1
    click element       id=${bianji}
    click nth element       id=${click}     1
    element should contain text     id=${delete}      (1/3)
#取消删除离线缓存
    click element       id=${delete}
    element should contain text     id=${deleteOrNot}       确定要删除吗
    click element       id=${quxiao}
    click element       id=${rightquxiao}
    ${tvnameb}          get nth element text    id=${tvname}   1
    should be equal     ${tvnamea}       ${tvnameb}
#编辑——逐个选中所有视频
    click element       id=${bianji}
    page should contain element     id=${click}
    element should contain text      id=${clickall}     全选
    element should contain text     id=${delete}       删除
    click nth element       id=${click}     1
    click nth element       id=${click}     2
    click nth element       id=${click}     3
    element should contain text     id=${delete}      (3/3)
    click element       id=${rightquxiao}
#删除离线缓存
    delete nth element      1

#删除所有离线缓存
    delete all element
    Page Should Not Contain Element     id=${tvname}
    element should contain text         id=${localempty}      没有下载的视频

