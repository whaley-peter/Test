*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/loginpage.py
Variables   eles/globaleles.py
Documentation   测试从开机屏跳转到注册界面、从注册界面跳转到登录界面功能

*** Test Cases ***
跳转到注册界面
    click element until no error    id=${registerbutton}
    element should contain text     id=${title}     注册微鲸账户
    input text      id=${usernameinput}     ${username}
    input text      id=${msm_code_input}    ${username}
    click element until no error        id=${nextstep}

    click element until no error    id=${jump_to_login_or_register}
    element should contain text     id=${title}     登录
    click back nth      2