*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/history.py
Variables           eles/globaleles.py
Variables           eles/minepage.py
Suite Setup         login and switch to debug mode
Suite Teardown      back to homepage
#Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     history
Force Tags           history

*** Test Cases ***
清空浏览历史--testhistory001
    delete all history

将视频加入到浏览历史--testhistory002
    [Documentation]  检查浏览历史
#浏览第一个视频
    wait until element is visible       id=${homepage}      10
    click element until no error        id=${homepage}
    click element until no error        xpath=${zongyi}
    wait until element is visible       xpath=${video1}     10
    click element until no error        xpath=${video1}
    page should contain element         id=${programname}
    ${tvdes1}       get text            id=${programname}
    sleep       20
    go back
#浏览第二个视频
    wait until element is visible       xpath=${video2}     10
    click element until no error        xpath=${video2}
    page should contain element         id=${programname}
    sleep       20
    go back
#浏览第三个视频
    wait until element is visible       xpath=${video3}     10
    click element until no error        xpath=${video3}
    page should contain element         id=${programname}
    sleep       20
    go back
#检查浏览历史
    wait until element is visible       id=${history}
    click element until no error        id=${history}
    page should contain element         xpath=${title}
    element should contain text         xpath=${title}       浏览历史
    ${hname}    get nth element text    id=${hname}          -1
    should be equal     ${tvdes1}       ${hname}

删除浏览历史--testhistory003
    [Documentation]  进行删除操作
#检查全选
    element should contain text in time     xpath=${bianjitext}     编辑
    click element until no error            id=${bianji}
    element should contain text             id=${clickall}          全选
    click element until no error            id=${clickall}
    is all selected
    click element until no error            id=${rightquxiao}
#删除一个
    delete nth element
#删除所有
    click back nth
    click element until no error            id=${history}
    delete all element
    click back nth
    click element until no error            id=${history}
    Page Should Not Contain Element         id=${hname}
    element should contain text in time     id=${hempty}       浏览记录为空