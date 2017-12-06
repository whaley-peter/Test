*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/history.py
Variables   eles/globaleles.py
Variables   eles/minepage.py
Suite Teardown       back to homepage

*** Test Cases ***
浏览历史1--testsearch001
        [Documentation]  检查浏览历史
#浏览第一个视频
        wait until element is visible       id=${homepage}      10
        click element   id=${homepage}
        click element   xpath=${zongyi}
        wait until element is visible   xpath=${video1}     10
        click element   xpath=${video1}
        page should contain element     id=${programname}
        ${tvdes1}       get text        id=${programname}
        sleep       20
        go back
#浏览第二个视频
        wait until element is visible   xpath=${video2}     10
        click element   xpath=${video2}
        page should contain element     id=${programname}
        sleep       20
        go back
#浏览第三个视频
        wait until element is visible   xpath=${video3}     10
        click element   xpath=${video3}
        page should contain element     id=${programname}
        sleep       20
        go back
#检查浏览历史
        wait until element is visible       id=${history}
        click element   id=${history}
        page should contain element         xpath=${title}
        element should contain text         xpath=${title}       浏览历史
        ${hname}       get nth element text    id=${hname}    -1
        should be equal     ${tvdes1}       ${hname}
浏览历史2--testsearch002
        [Documentation]  进行删除操作
#检查全选
        page should contain element         id=${bianji}
        click element       id=${bianji}
        element should contain text       id=${clickall}        全选
        click element       id=${clickall}
        is all selected
        click element      id=${rightquxiao}
#删除一个
        delete nth element      1
#删除所有
        delete all element
        Page Should Not Contain Element     id=${hname}
        element should contain text         id=${hempty}       浏览记录为空