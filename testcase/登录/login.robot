*** Settings ***
Library    libs/AppiumExtend.py
Variables  libs/cfg.py
Variables  eles/homepage.py
Force Tags      login
*** Test Cases ***
登录-testlogin001
    [tags]      login
    open application     http://localhost:4723/wd/hub     platformName=Android    platformVersion=6.0    deviceName=VGYP7T6P99999999    app=E:/Test/app/WhaleyVR.apk    appPackage=com.snailvr.manager
    wait until element is visible       id=com.snailvr.manager:id/btn_login     10
    click element       id=com.snailvr.manager:id/btn_login
    Input Text          id=com.snailvr.manager:id/et_user_name    18616512272
    Input Text          id=com.snailvr.manager:id/et_password    a123456
    click element       id=com.snailvr.manager:id/btn_login
    wait until element is visible       id=${homebase}      10
    swipe left nth     2



