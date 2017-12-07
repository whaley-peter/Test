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
        click element       xpath=${usehelp}
#检查界面
        wait until element is visible   xpath=${title}      5
        element should contain text in time     xpath=${title}        帮助