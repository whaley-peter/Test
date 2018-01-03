*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/minepage.py
Variables           eles/globaleles.py
Variables           eles/loginpage.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
#Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     myvoucher
Force Tags          myvoucher

*** Test Cases ***
我的券/兑换码遍历--testmyvoucher001
    [Documentation]  我的券/兑换码界面遍历
    click element until no error                id=${mybase}
    wait until element is visible               xpath=${mycoupen}       10
    click element until no error                xpath=${mycoupen}
    element should contain text in time         xpath=${title}          我的券/兑换码
# 检查兑换码输入框
    page should contain element                 id=${mabox}
    element should contain text in time         xpath=${maname}         请输入兑换码
#检查购买明细
    page should contain element                 id=${mingxi}
    click element until no error                id=${mingxi}
    element should contain text in time         xpath=${title}          购买明细
    click back nth     2
退出登录，从我的券/兑换码登录--testmyvoucher002
    [Documentation]  退出登录并通过我的券/兑换码登录
#退出登录
    logout
#从我的券/兑换码登录
    wait until element is visible               xpath=${mycoupen}       10
    click element until no error                xpath=${mycoupen}
    page should contain element                 id=${content}
    click element until no error                id=${confirm}
    input text                                  id=${usernameinput}     ${username}
    input text                                  id=${passwordinput}     ${password}
    click element until no error                id=${loginbutton}
    wait until element is visible               xpath=${title}          5
    element should contain text in time         xpath=${title}          我的券/兑换码