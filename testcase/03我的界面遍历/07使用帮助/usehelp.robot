*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags      usehelp

*** Test Cases ***
使用帮助--testfeedback001
        click element       id=${mybase}
        swipe up nth      2
        click element       xpath=${usehelp}
#检查界面
        element should contain text     id=${title}        帮助