*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Force Tags  localvideo
*** Test Cases ***
相册视频导入-testlocalvideo001
    [Documentation]   导入相册中的视频
    click element     id=${mybase}
    click element     xpath=${localmanagement}
    swipe left nth
    click element     id=${xiangce}
    click nth element       id=${layout}     2
    ${videoname1}      get nth element text     id=${layname}      2
    click element       id=${daoru}
    click element       id=${ok}
    ${videoname2}      get nth element text     id=${videoname}      -1
    should be equal     ${videoname1}       ${videoname2}

删除操作1-testlocalvideo002
    [Documentation]   取消删除和删除一个操作
#取消删除
    click element      id=${bianji}
    click nth element      id=${check}      1
    click element      id=${delete}
    click element      id=${quxiao}
    click element      id=${rightquxiao}
#删除一个
    delete nth element      1
    page should not contain element     id=${videoname}

删除操作2-testlocalvideo003
    [Documentation]     删除所有操作
#删除所有
#    click element       id=${xiangce}
#    click nth element       id=${layout}    2
#    click nth element       id=${layout}   1
#    click element       id=${daoru}
#    click element       id=${ok}

    delete all element
#    Page Should Not Contain Element     id=${videoname}
    element should contain text         id=${localempty}      没有本地视频
链接导入-testlocalvideo004
    [Documentation]     检查链接导入界面
    click element       id=${link}
    element should contain text         id=${title}          链接导入
    page should contain element         id=${suggestion}
    page should contain element         id=${daoru}


