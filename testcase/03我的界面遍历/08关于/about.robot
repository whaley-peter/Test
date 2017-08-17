*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
使用帮助--testfeedback001
        click element       id=${mybase}
        swipe up nth      2
        click element       id=${about}
#检查界面
        page should contain element     id=${icon}
        page should contain element     id=${enter}
        page should contain element     id=${trade}

        click element       id=${agreement}
        element should contain text     id=${title5}        用户协议