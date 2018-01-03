*** Settings ***
Library             libs/AppiumExtend.py
Variables           eles/minepage.py
Variables           eles/globaleles.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
#Test Setup          kill logcat         ${udid}
#Test Teardown       run keyword if test failed       logcat     ${udid}     mygift
Force Tags          mygift

*** Test Cases ***
我的奖品--testmygift001
    [Documentation]  在我的奖品界面添加地址
    click element until no error                id=${mybase}
    wait until element is visible               xpath=${mygift}            10
    click element until no error                xpath=${mygift}
#检查界面
    wait until element is visible               xpath=${title}             5
    element should contain text in time         xpath=${title}             我的奖品
    page should contain element                 id=${address}
    click element until no error                id=${address}
#  修改地址界面
    page should contain element                 xpath=${title}
    element should contain text in time         xpath=${title}             修改地址
    element should contain text in time         xpath=${shouhuoren}        收货人
    element should contain text in time         xpath=${dianhua}           联系电话
    element should contain text in time         xpath=${dizhi}             所在地址
    element should contain text in time         xpath=${xiangxi}           详细地址
#添加收货人
    click element until no error                id=${etname}
    input text          id=${etname}            lutaitai
#添加联系电话
    click element until no error                id=${etnumber}
    input text          id=${etnumber}          18701870187
#选择所在地址
    click element until no error                id=${etaddress}
    element should contain text in time         id=${province}              选择所在省份
    click element until no error                xpath=${shanghai}
    click element until no error                xpath=${changning}
    click element until no error                xpath=${chengqu}
#添加详细地址
    wait until element is visible               id=${fulladdress}           10
    click element until no error                id=${fulladdress}
    input text          id=${fulladdress}       waitanshibahao
    wait until element is visible               id=${submit}                10
    click element until no error                id=${submit}
    go back
    element should contain text in time         xpath=${title}              我的奖品