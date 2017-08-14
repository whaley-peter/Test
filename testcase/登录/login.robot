*** Settings ***
Library    libs/AppiumExtend.py
Variables  libs/cfg.py
Variables  eles/homepage.py
Variables  eles/login.py
Variables  eles/globaleles.py

*** Test Cases ***
登录界面跳转到注册--testdenglu001
    open application    ${remote_server}    ${desired_caps}
    click element until no error        id=${loginbutton}
    click element until no error        id=${rigister}
    element should contain text         id=${title}     注册微鲸账户
    click back nth      1

登录界面跳转到短信--testdenglu002
    click element until no error        id=${safe_login}
    element should contain text         id=${title}     短信快捷登录
    click back nth      1

登录界面跳转到忘记密码--testdenglu003
    click element until no error    id=${forget_pwd}
    element should contain text     id=${title}     找回密码
    click back nth      1

登录app---testdenglu001
    click element       id=${loginbutton}
    Input Text          id=${user_name}    ${username}
    Input Text          id=${password}     ${password}
    click element       id=${loginbutton}
    wait until element is visible       id=${homebase}      10




