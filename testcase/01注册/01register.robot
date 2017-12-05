*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/loginpage.py
Variables   eles/globaleles.py
Variables   eles/minepage.py
Suite Setup     back to homepage
Suite Teardown  back to homepage
Force Tags  zhuce
Documentation   测试从开机屏跳转到注册界面、从注册界面跳转到登录界面功能

*** Test Cases ***
从注册界面跳转到登录界面--testregister001
    click element until no error    id=${registerbutton}
    element should contain text     xpath=${title}     注册微鲸账户
    click element until no error    id=${jump_to_login_or_register}
    element should contain text     xpath=${title}     登录
    click back nth


在注册界面，点击注册--testregister002
    input text      id=${usernameinput}     ${username}
    input text      id=${msm_code_input}    ${username}
    click element until no error        id=${nextstep}
    click back nth

测试
    [Tags]  ceshi
#    click element until no error    id=${leapfrog}
    sleep   5
    click element until no error    id=${mybase}
    ${test}     get text        xpath=${tvtext}
    log to console      ${test}
