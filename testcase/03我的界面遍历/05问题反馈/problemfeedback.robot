*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags      wentifankui

*** Test Cases ***
问题反馈--testfeedback001
        click element       id=${mybase}
        click element       xpath=${problemfeedback}
#检查界面
        element should contain text     id=${title}        问题反馈


