*** Settings ***
Library     libs/AppiumExtend.py
Variables       eles/homepage.py
Force Tags      zhuanti

*** Test Cases ***
点击首页推荐位元素--testzhuanti001
    wait until element is visible       id=${homebase}      10
    swipe left nth     1
    click nth element       xpath=${recommend_eles}     1
    sleep   5
    click element       id=com.snailvr.manager:id/btn_back
    sleep   2
