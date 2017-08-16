*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Suite Teardown       back to homepage
Force Tags  localvideo

*** Test Cases ***
相册视频导入-testlocalvideo001

    click element     id=${mybase}
    click element     id=${localmanagement}
    click element     id=${xiangce}
    click nth element       id=com.snailvr.manager:id/pic_layout     2
    ${videoname1}      get nth element text     id=com.snailvr.manager:id/name      2
    click element       id=${daoru}
    click element       id=${ok}
    ${videoname2}      get nth element text     id=com.snailvr.manager:id/name      -1

    should be equal     ${videoname1}       ${videoname2}
删除操作1-testlocalvideo002

#取消删除
    click element      id=${bianji}
    click element      id=${check}
    click element      id=${delete}
    click element      id=${quxiao}

#删除一个
    click element       id=${delete}
    click element       id=${confirm}
    page should not contain element     id=${videoname}

删除操作2-testlocalvideo003
#删除所有
    click element     id=${xiangce}
    click nth element       id=com.snailvr.manager:id/pic_layout    2
    click element       id=${daoru}
    click element       id=${ok}

    click element     id=${xiangce}
    click nth element       id=com.snailvr.manager:id/pic_layout   1
    ${videoname3}      get nth element text     id=com.snailvr.manager:id/name      1
    click element       id=${daoru}
    click element       id=${ok}
    ${videoname4}      get nth element text     id=com.snailvr.manager:id/name      -1
    should be equal     ${videoname3}       ${videoname4}


    click element       id=${bianji}
    click element       id=${checkall}
    click element       id=${delete}
    click element       id=${confirm}

    Page Should Not Contain Element     id=${videoname}
链接导入-testlocalvideo004
    click element       id=${link}


