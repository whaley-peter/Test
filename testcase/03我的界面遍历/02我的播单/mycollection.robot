*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
加入我的播单--testwodebodan001
    click element   id=${homepage}
    click element   xpath=${zongyi}
    sleep      3
    ${tvdes1}       get nth element text    id=${tvdes}     1
    click element   xpath=${video1}
    click element   id=${collectbodan}
    click element   id=${backbutton}
    sleep      2

    ${tvdes2}       get nth element text    id=${tvdes}     2
    click element  xpath=${video2}
    click element   id=${collectbodan}
    sleep  4
    click element   id=${backbutton}

#进入检查我的播单
    click element       id=${mybase}
    click element       id=${mycollection}
    ${boname1}       get nth element text    id=${bodanname}   2
    should be equal     ${tvdes1}       ${boname1}
    ${boname2}       get nth element text    id=${bodanname}   1
    should be equal     ${tvdes2}       ${boname2}

#取消删除播单
    click element       id=${bianji}
    click element       id=${check}
    click element       id=${delete}
    click element       id=${quxiao}
    click element       id=${rightquxiao}

#删除播单
    delete nth element      1

#删除所有播单
    delete all element
    Page Should Not Contain Element     id=${bodanvideo}
    click nth element until no error    id=${mycollection}
#    click element until no error        id=${backbutton}
#    click element        id=${backbutton}
