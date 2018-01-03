*** Settings ***
Library         libs/AppiumExtend.py
Variables       eles/globaleles.py
Suite Setup     open application       ${remote server}     ${desired caps}
Suite Teardown  kill uiautomator and logcat
#Suite Setup      open mutilapplications            ${remote_url}      ${udid}
#Suite Teardown   kill uiautomator and logcat       ${udid}
Force Tags       testapp
