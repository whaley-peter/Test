*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
问题反馈--testfeedback001
        click element       id=${mybase}
        click element       id=${problemfeedback}
#检查界面
        element should contain text     id=${title3}        问题反馈