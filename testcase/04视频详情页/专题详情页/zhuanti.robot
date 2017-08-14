*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/homepage.py
Variables   eles/minepage.py
*** Test Cases ***
点击首页推荐位元素--testzhuanti001
    wait until element is visible       id=${homebase}      10
    swipe left nth     1
    click nth element       id=com.snailvr.manager:id/tv_label     1
    element should contain text     id=com.snailvr.manager:id/tv_name       蒙面唱将第二期
    swipe up nth      3
    click element       id=com.snailvr.manager:id/btn_back
    sleep   2
