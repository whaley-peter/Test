*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/history.py
Variables   eles/globaleles.py
Variables   eles/minepage.py
Suite Teardown       back to homepage

*** Test Cases ***
浏览历史--testsearch001
        [Documentation]  检查浏览历史以及进行删除操作
#浏览视频
        click element   id=${homepage}
        click element   xpath=${zongyi}
        wait until element is visible   xpath=${video1}
        click element   xpath=${video1}
        ${tvdes1}       get text        id=${programname}
        sleep       20
        go back
        wait until element is visible   xpath=${video2}
        click element   xpath=${video2}
        sleep       20
        go back
#检查浏览历史
        click element   id=${history}
        element should contain text         id=${title}       浏览历史
        ${hname}       get nth element text    id=${hname}    -1
        should be equal     ${tvdes1}       ${hname}
#删除一个
        delete nth element      1
#删除所有
        delete all element
        Page Should Not Contain Element     id=${hname}
        element should contain text         id=${hempty}       浏览记录为空