*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/globaleles.py
#Suite Setup     open application       ${remote server}     ${desired caps}
#Suite Teardown  kill uiautomator
Force Tags      testapp
