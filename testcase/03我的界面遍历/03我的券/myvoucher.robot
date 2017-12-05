*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Variables   eles/loginpage.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags      myvoucher

*** Test Cases ***
我的券/兑换码遍历--testmyvoucher001
        [Documentation]  我的券/兑换码界面遍历
        click element       id=${mybase}
        wait until element is visible       xpath=${mycoupen}          10
        click element       xpath=${mycoupen}
        page should contain element         xpath=${title}
        element should contain text         xpath=${title}          我的券/兑换码
# 检查兑换码输入框
        page should contain element         id=${mabox}
        element should contain text         xpath=${maname}       请输入兑换码
#检查是否有观看券
#        page should contain element         id=${quanname}
#检查购买明细
        page should contain element         id=${mingxi}
        click element       id=${mingxi}
        element should contain text         xpath=${title}           购买明细
#检查购买数量
#        page should contain element         id=${paynum}
         click back nth     2
退出登录，从我的券/兑换码登录--testmyvoucher002
    [Documentation]  退出登录并通过我的券/兑换码登录
#退出登录
    wait until element is visible       id=${settingbutton}         10
    logout
#从我的券/兑换码登录
    wait until element is visible       xpath=${mycoupen}           10
    click element       xpath=${mycoupen}
    page should contain element         id=${content}
    click element       id=${confirm}
    element should contain text         xpath=${title}         登录
    input text          id=${usernameinput}         18616512272
    input text          id=${passwordinput}         a123456
    click element       id=${loginbutton}
#    page should contain element         xpath=${title}
#    element should contain text         xpath=${title}          我的券/兑换码