*** Settings ***
Library         libs/AppiumExtend.py
Variables       eles/minepage.py
Variables       eles/videodetailspage.py
Variables       eles/globaleles.py
Suite Setup     back to homepage
Suite Teardown  back to homepage
Test Setup          kill logcat         ${udid}
Test Teardown       run keyword if test failed       logcat     ${udid}     localcache
Force Tags      localcache

*** Test Cases ***
选择视频进行缓存-testlocalcache001
    [Documentation]  选择视频进行缓存后进入本地管理-离线缓存检查视频
    click element until no error     id=${homepage}
    click element until no error     xpath=${zongyi}
#缓存第一个视频
    wait until element is visible    xpath=${video1}
    click element until no error     xpath=${video1}
    ${tvdes1}       get text         id=${programname}
    click element until no error     id=${download}
    wait until element is visible    xpath=${downloadtext1}      10
    ${val}      get text             xpath=${downloadtext1}
    should be equal     ${val}       已缓存
#缓存第二个视频
    click back nth
    wait until element is visible   xpath=${video2}
    click element until no error    xpath=${video2}
    click element until no error    id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text            xpath=${downloadtext1}
    should be equal     ${val}      已缓存
#缓存第三个视频
    click back nth
    wait until element is visible   xpath=${video3}
    click element until no error    xpath=${video3}
    click element until no error    id=${download}
    wait until element is visible   xpath=${downloadtext1}      10
    ${val}      get text            xpath=${downloadtext1}
    wait until element is visible   xpath=${downloadtext1}      10
    should be equal        ${val}       已缓存
#检查离线缓存
    click back nth
    swipe right nth     3
    click element until no error             id=${mybase}
    click element until no error             xpath=${localmanagement}
    element should contain text in time      id=${title}     本地
    ${tvname1}       get nth element text    id=${tvname}    -1
    should be equal     ${tvdes1}            ${tvname1}

取消和删除离线缓存-testlocalcache002
    [Documentation]  对离线缓存进行删除一个或多个的操作
    ${tvnamea}       get nth element text   id=${tvname}        1
    click element until no error            id=${bianji}
    element should contain text in time     id=${clickall}      全选
    click nth element                       id=${click}         1
    element should contain text in time     id=${delete}        删除 (1/3)
#取消删除离线缓存
    click element until no error            id=${delete}
    click element until no error            id=${quxiao}
    go back
    ${tvnameb}    get nth element text      id=${tvname}        1
    should be equal     ${tvnamea}          ${tvnameb}
#编辑——逐个选中所有视频
    click element until no error            id=${bianji}
    click nth element                       id=${click}         1
    click nth element                       id=${click}         2
    click nth element                       id=${click}         3
    element should contain text in time     id=${clickall}      取消全选
    element should contain text in time     id=${delete}        删除 (3/3)
    click element until no error            id=${rightquxiao}
#删除离线缓存
    delete nth element      1

#删除所有离线缓存
    delete all element
    Page Should Not Contain Element         id=${tvname}
    element should contain text in time     id=${localempty}      没有下载的视频
    page should not contain element         id=${bianji}

