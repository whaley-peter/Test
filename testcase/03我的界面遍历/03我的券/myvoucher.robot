*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
我的券/兑换码遍历--testmyvoucher001
        click element       id=${mybase}
        click element       id=${mycoupen}
# 检查兑换码输入框
        page should contain element         id=${mabox}
        element should contain text         xpath=${maname}       请输入兑换码
#检查是否有观看券
#        page should contain element         id=${quanname}
#检查购买明细
        click element       id=${mingxi}
        element should contain text         id=${title}           购买明细
#        page should contain element         id=${paynum}