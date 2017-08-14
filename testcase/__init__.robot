*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/globaleles.py
Suite Setup     open application       ${remote server}     ${desired caps}
Force Tags      testapp
#Suite Teardown