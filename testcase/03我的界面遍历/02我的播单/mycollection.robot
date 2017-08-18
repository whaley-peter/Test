*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
加入我的播单--testwodebodan001
    [Documentation]  加入播单后在我的播单进行删除操作
#加入播单
    click element   id=${homepage}
    click element   xpath=${zongyi}
    wait until element is visible   xpath=${video1}
    click element   xpath=${video1}
    ${tvdes1}       get text        id=${programname}

    click element   id=${collectbodan}
    click element   id=${backbutton}

    wait until element is visible   xpath=${video2}
    click element   xpath=${video2}
    click element   id=${collectbodan}
    click element   id=${backbutton}

#进入检查我的播单
    click element       id=${mybase}
    click element       id=${mycollection}
    ${boname1}       get nth element text    id=${bodanname}   2
    should be equal     ${tvdes1}       ${boname1}

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
    element should contain text         id=${mycollectionempty}         暂无视频加入播单
