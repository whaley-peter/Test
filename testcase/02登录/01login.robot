*** Settings ***
Library    libs/AppiumExtend.py
Variables  eles/homepage.py
Variables  eles/loginpage.py
Variables  eles/globaleles.py
Variables  eles/minepage.py
Documentation   测试登录功能、登录界面跳转到其他界面功能

*** Test Cases ***
登录界面跳转到注册--testdenglu001
    click element until no error        id=${loginbutton}
    click element until no error        id=${jump_to_login_or_register}
    element should contain text         id=${title}     注册微鲸账户
    click back nth      1

登录界面跳转到短信--testdenglu002
    click element until no error        id=${safe_login}
    element should contain text         id=${title}     短信快捷登录
    click back nth      1

登录界面跳转到忘记密码--testdenglu003
    click element until no error    id=${forget_pwd}
    element should contain text     id=${title}     找回密码
    click back nth      2

登录app---testdenglu004
    login       ${username1}     ${password1}
    wait until element is visible       id=${homebase}      10
    click element until no error        id=${mybase}
    element should contain text     id=${nickname}      ${usernickname1}
    logout





