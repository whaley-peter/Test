*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globalEles.py

*** Test Cases ***
进入我的播单
    click element    id=${mybase}
    click element    id=${mycollection}

    click nth element until no error        id=com.snailvr.manager:id/layout_collect        6
    click element until no error        id=${backbutton}
    click element        xpath=//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=6]
    click element        id=${backbutton}
