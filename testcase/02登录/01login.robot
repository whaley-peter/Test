*** Settings ***
Library    libs/AppiumExtend.py
Variables  eles/homepage.py
Variables  eles/loginpage.py
Variables  eles/globaleles.py
Variables  eles/minepage.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
#Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     denglu
Force Tags          denglu
Documentation       测试登录功能、登录界面跳转到其他界面功能

*** Test Cases ***
检查登录界面文字显示--testdenglu001
    element should contain text in time     id=${loginbutton}                登录
    click element until no error            id=${loginbutton}
    element should contain text in time     xpath=${title}                   登录
    element should contain text in time     xpath=${usernameinput_text}      请输入您的手机号码
    element should contain text in time     id=${safe_login}                 短信快捷登录
    element should contain text in time     id=${forget_pwd}                 忘记密码
    element should contain text in time     id=${loginbutton}                登录
    element should contain text in time     id=${third app title}            使用社交平台登录/注册
    element should contain text in time     xpath=${jump to login or register text}     注册

登录界面跳转到注册--testdenglu002
    click element until no error            id=${jump_to_login_or_register}
    element should contain text in time     xpath=${title}                  注册微鲸账户
    click back nth

登录界面跳转到短信--testdenglu003
    click element until no error            id=${safe_login}
    element should contain text in time     xpath=${title}                  短信快捷登录
    element should contain text in time     xpath=${registerinput_text}     请输入您的手机号码
    element should contain text in time     xpath=${msm_code_input_text}    请输入安全码
    element should contain text in time     id=${msm_code_get}              获取安全码
    element should contain text in time     id=${next_step}                 下一步
    click back nth

登录界面跳转到忘记密码--testdenglu004
    click element until no error            id=${forget_pwd}
    element should contain text in time     xpath=${title}                  找回密码
    element should contain text in time     xpath=${registerinput_text}     请输入您的手机号码
    element should contain text in time     xpath=${msm_code_input_text}    请输入安全码
    element should contain text in time     id=${msm_code_get}              获取安全码
    element should contain text in time     id=${next_step}                 下一步
    element should contain text in time     id=${connect_us}                联系我们
    click element until no error            id=${connect_us}
    element should contain text in time     xpath=${title}                  微鲸VR公司简介_联系方式_微鲸VR企业招聘-微鲸VR官方网站
    click back nth      3

登录app---testdenglu005
    login       ${username1}     ${password1}
    wait until element is visible           id=${homebase}      10
    click element until no error            id=${mybase}
    element should contain text in time     id=${nickname}      ${usernickname1}
    logout





