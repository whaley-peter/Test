*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/minepage.py
Variables           eles/globaleles.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
Test Setup          kill logcat         ${udid}
Test Teardown       run keyword if test failed       logcat     ${udid}     about
Force Tags          about

*** Test Cases ***
关于微鲸VR--testabout001
        click element until no error            id=${mybase}
        click element until no error            xpath=${about}
#检查界面
        wait until element is visible           xpath=${title}      5
        element should contain text in time     xpath=${title}      关于微鲸VR
        page should contain element             id=${icon}
        element should contain text in time     id=${enter}         加入官方QQ粉丝群：170321770
        element should contain text in time     id=${trade}         商务合作
        element should contain text in time     id=${agreement}     用户协议
        click element until no error            id=${trade}
        element should contain text in time     xpath=${title}      商务合作
        click back nth
        click element until no error            id=${agreement}
        element should contain text in time     xpath=${title}      用户协议