*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py

*** Test Cases ***
跳转到我的界面-testlocal001
    click element     id=${mybase}

    click element     id=${localvideo}