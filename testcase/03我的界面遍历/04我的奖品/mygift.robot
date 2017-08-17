*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
我的奖品--testmygift001
        click element       id=${mybase}
        click element       id=${mygift}
#检查界面
        element should contain text         id=${title2}        我的奖品
        page should contain element         id=${address}
#添加地址
        click element       id=${address}
        click element       id=${etname}
        clear text          id=${etname}
        input text          id=${etname}        lutaitai

        click element       id=${etnumber}
        clear text          id=${etnumber}
        input text          id=${etnumber}      18701870187

        click element       id=${etaddress}
        click element       xpath=${shanghai}
        click element       xpath=${changning}
        click element       xpath=${chengqu}

        click element       id=${fulladdress}
        clear text          id=${fulladdress}
        input text          ${fulladdress}      waitanshibahao
        go back

        click element       id=${submit}