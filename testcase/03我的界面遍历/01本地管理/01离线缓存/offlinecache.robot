*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py

*** Test Cases ***
选择视频进行缓存-testlocalcache001
    click element   id=${homepage}
    click element   xpath=${zongyi}

检查离线缓存-testlocalcache001
    click element     id=${mybase}
    click element     id=${localmanagement}
    click element     class=${offlinecache}

    element should contain text     id=${tvname}     汪苏泷-《I Believe2》

取消删除离线缓存-testlocalcache002
 #   click element     id=${mybase}
 #   click element     id=${localmanagement}
 #   click element     class=${offlinecache}

    click element       id=${bianji}
    click element       id=${check}
    click element       id=${delete}
    click element       id=${quxiao}
    element should contain text     id=${tvname}     汪苏泷-《I Believe2》

#删除离线缓存
    click element       id=${delete}
    click element       id=${confirm}
    page should not contain element      id=${tvname}

删除所有离线缓存-testlocalcache003
    click element     id=${mybase}
    click element     id=${localmanagement}
    click element     xpath=${offlinecache}

    click element       id=${bianji}
    click element       id=${checkall}

    click element       id=${delete}
    click element       id=${confirm}
    Page Should Not Contain Element     id=${tvname}

