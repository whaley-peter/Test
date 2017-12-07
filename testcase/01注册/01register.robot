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
检查注册界面文字显示--testregister001
    element should contain text in time     id=${registerbutton}            注册
    click element until no error            id=${registerbutton}
    element should contain text in time     xpath=${title}                  注册微鲸账户
    element should contain text in time     xpath=${registerinput_text}     请输入您的手机号码
    element should contain text in time     xpath=${msm_code_input_text}    请输入安全码
    element should contain text in time     id=${msm_code_get}              获取安全码
    element should contain text in time     id=${next_step}                 下一步
    element should contain text in time     id=${third_app_title}           使用社交平台登录/注册

从注册界面跳转到登录界面--testregister002
    click element until no error    id=${jump_to_login_or_register}
    element should contain text in time     xpath=${title}                  登录
    click back nth

在注册界面，点击注册--testregister003
    input text      id=${registerinput}     ${username}
    input text      id=${msm_code_input}    ${username}
    click element until no error        id=${nextstep}
    click back nth
