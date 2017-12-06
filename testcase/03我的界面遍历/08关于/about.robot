*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags      about

*** Test Cases ***
关于微鲸VR--testabout001
        click element       id=${mybase}

        element should contain text     xpath=${abouttext1}     关于
        element should contain text     xpath=${abouttext2}     加入官方粉丝群
        click element       xpath=${about}
#检查界面
        wait until element is visible   xpath=${title}      5
        element should contain text     xpath=${title}      关于微鲸VR
        page should contain element     id=${icon}
        element should contain text     id=${enter}        加入官方QQ粉丝群：170321770
        element should contain text     id=${trade}        商务合作
        element should contain text     id=${agreement}    用户协议
        click element until no error    id=${trade}
        element should contain text     xpath=${title}        商务合作
        click back nth
        click element       id=${agreement}
        element should contain text     xpath=${title}        用户协议