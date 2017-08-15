*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/minepage.py
Variables   eles/globaleles.py

*** Test Cases ***
进入我的播单--testwodebodan001
    click element    id=${mybase}
    click element    id=${mycollection}
    click nth element until no error    id=${mycollection}
    click element until no error        id=${backbutton}
    click element        id=${backbutton}
