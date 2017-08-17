*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
使用帮助--testfeedback001
        click element       id=${mybase}
        swipe up nth      2
        click element       id=${usehelp}
#检查界面
        element should contain text     id=${title4}        帮助