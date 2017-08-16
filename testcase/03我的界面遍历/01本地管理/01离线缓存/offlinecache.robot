*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/videodetailspage.py
Variables   eles/globaleles.py
*** Test Cases ***
选择视频进行缓存-testlocalcache001
    click element   id=${homepage}
    click element   xpath=${zongyi}
    sleep      3
    ${tvdes1}       get nth element text    id=${tvdes}     1
    click element   xpath=${video1}
    click element   id=${download}

#    ${val}      get text     xpath=${downloadtext}    //也可以断言
#    should be equal        ${val}      已缓存         //也可以断言
    sleep      2
#    element should contain text     xpath=${downloadtext}       已缓存
    click element   id=${backbutton}
    sleep      2
    ${tvdes2}       get nth element text    id=${tvdes}     2
    click element  xpath=${video2}
    click element   id=${download}
#    element should contain text     xpath=${downloadtext}       已缓存
    click element   id=${backbutton}


#检查离线缓存
    click element     id=${mybase}
    click element     id=${localmanagement}
    click nth element     class=${offlinecache}         1

    ${tvname1}       get nth element text    id=${tvname}   2
    should be equal     ${tvdes1}       ${tvname1}
    ${tvname2}       get nth element text    id=${tvname}   1
    should be equal     ${tvdes2}       ${tvname2}

取消和删除离线缓存-testlocalcache002
#取消删除离线缓存
    click element       id=${bianji}
    click element       id=${check}
    click element       id=${delete}
    click element       id=${quxiao}
    click element       id=${rightquxiao}

#删除离线缓存
    delete nth element      1

#删除所有离线缓存
    delete all element
    Page Should Not Contain Element     id=${tvname}

