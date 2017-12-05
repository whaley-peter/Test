*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py
Suite Setup     back to homepage
Suite Teardown       back to homepage
Force Tags      mygift

*** Test Cases ***
我的奖品--testmygift001
        [Documentation]  在我的奖品界面添加地址
        click element       id=${mybase}
        wait until element is visible       xpath=${mygift}         10
        click element       xpath=${mygift}
#检查界面
        element should contain text         xpath=${title}             我的奖品
        page should contain element         id=${address}
        click element       id=${address}
#  修改地址界面
        page should contain element         xpath=${title}
        element should contain text         xpath=${title}             修改地址
        element should contain text         xpath=${shouhuoren}        收货人
        element should contain text         xpath=${dianhua}           联系电话
        element should contain text         xpath=${dizhi}             所在地址
        element should contain text         xpath=${xiangxi}           详细地址
#添加收货人
        page should contain element         id=${etname}
        click element       id=${etname}
        clear text          id=${etname}
        input text          id=${etname}        lutaitai
#添加联系电话
        click element       id=${etnumber}
        clear text          id=${etnumber}
        input text          id=${etnumber}      18701870187
#选择所在地址
        click element       id=${etaddress}
        page should contain element         id=${content}
        click element       xpath=${shanghai}
        click element       xpath=${changning}
        click element       xpath=${chengqu}
#添加详细地址
        wait until element is visible       id=${fulladdress}           10
        click element       id=${fulladdress}
        clear text          id=${fulladdress}
        input text          ${fulladdress}      waitanshibahao
        go back
        wait until element is visible       id=${submit}                10
        click element       id=${submit}
        page should contain element         xpath=${title}
        element should contain text         xpath=${title}             我的奖品
