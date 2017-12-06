*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags  localvideo

*** Test Cases ***
相册视频导入-testlocalvideo001
    [Documentation]   导入相册中的视频
#检查界面
    click element     id=${mybase}
    page should contain element     xpath=${localmanagement}
    click element     xpath=${localmanagement}
    wait until element is visible   xpath=${title}      5
    element should contain text     xpath=${title}      本地
    sleep   3
    swipe left nth
    delete all element
    page should contain element     id=${xiangce}
    click element     id=${xiangce}
    element should contain text         xpath=${title}          相册视频导入
    element should contain text     id=${clickall}      全选
    element should contain text     id=${daoru}     导入

#导入一个视频
    click nth element       id=${layout}     2
    ${videoname1}      get nth element text     id=${layname}      2
    click element       id=${daoru}
    element should contain text     id=${content}       导入完成
    element should contain text     id=${content}       请前往“本地”-“本地视频”
    element should contain text     id=${content}       查看已导入的视频
    element should contain text     id=${ok}        确定
    click element       id=${ok}
    ${videoname2}      get nth element text     id=${videoname}      -1
    should be equal     ${videoname1}       ${videoname2}
#导入所有视频
    click element     id=${xiangce}
    element should contain text         xpath=${title}          相册视频导入
    click element     id=${clickall}
    is all selected
    click element       id=${daoru}
    click element       id=${ok}

删除操作1-testlocalvideo002
    [Documentation]   取消删除和删除一个操作
#取消删除
    element should contain text     xpath=${bianjitext}    编辑
    click element      id=${bianji}
    click nth element      id=${click}      1
    click element      id=${delete}
    element should contain text     id=${content}       继续操作将会
    element should contain text     id=${content}       从列表里移除选中的视频，
    element should contain text     id=${content}       确定继续吗？
    element should contain text     id=${quxiao}        取消
    click element      id=${quxiao}
    click element      id=${rightquxiao}
#删除一个
    element should contain text     xpath=${bianjitext}    编辑
    ${videonamea}      get nth element text     id=${videoname}      1
    delete nth element      1
    ${videonameb}      get nth element text     id=${videoname}      1
    should not be equal     ${videonamea}       ${videonameb}

删除操作2-testlocalvideo003
    [Documentation]     删除所有操作
    element should contain text     xpath=${bianjitext}    编辑
    delete all element
    page should not contain element     id=${bianji}
    element should contain text         id=${localempty}      没有本地视频
链接导入-testlocalvideo004
    [Documentation]     检查链接导入界面
    click element       id=${link}
    element should contain text         xpath=${title}          链接导入
    element should contain text         id=${suggestion}        请输入视频链接
    page should contain element         id=${linkimport}
    input text          id=${suggestion}        http://vr.moguv.com/play/5dacf3e06a154ac4a3397293128ce38a
    click element       id=${linkimport}
    page should contain element         id=${picvideo}