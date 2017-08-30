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

    wait until element is visible   xpath=${video1}
    click element   xpath=${video1}
    ${tvdes1}       get text        id=${programname}
    click element   id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text     xpath=${downloadtext1}
    should be equal        ${val}       已缓存

    click back nth
    wait until element is visible   xpath=${video2}
    click element   xpath=${video2}
    click element   id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text     xpath=${downloadtext1}
    wait until element is visible   xpath=${downloadtext1}
    should be equal        ${val}       已缓存
    click back nth
#检查离线缓存
    click element     id=${mybase}
    click element     xpath=${localmanagement}
    ${tvname1}       get nth element text    id=${tvname}   2
    should be equal     ${tvdes1}       ${tvname1}

取消和删除离线缓存-testlocalcache002
    [Documentation]  对离线缓存进行删除一个或多个的操作
#取消删除离线缓存
    click element       id=${bianji}
    click nth element       id=${check}     1
    click element       id=${delete}
    click element       id=${quxiao}
    click element       id=${rightquxiao}

#删除离线缓存
    delete nth element      1

#删除所有离线缓存
    delete all element
    Page Should Not Contain Element     id=${tvname}
    element should contain text         id=${localempty}      没有下载的视频

