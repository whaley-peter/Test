*** Settings ***
Library         libs/AppiumExtend.py
Variables       eles/minepage.py
Variables       eles/globaleles.py
Suite Setup     back to homepage
Force Tags      mypagescan

*** Test Cases ***
遍历我的界面所有元素
    wait until element is visible           id=${mybase}        10
    click element until no error            id=${mybase}
    element should contain text in time     id=${mybase}                            我
    element should contain text in time     id=${nickname}                          ${usernickname}
    element should contain text in time     id=${info}                              个人信息
    element should contain text in time     xpath=${whaleyCurrency_text}            鲸币
    element should contain text in time     xpath=${mycoupen_text}                  兑换码/券
    element should contain text in time     xpath=${mygift_text}                    我的奖品
    element should contain text in time     xpath=${localmanagement_text_left}      本地管理
    element should contain text in time     xpath=${localmanagement_text_right}     万能VR播放器
    element should contain text in time     xpath=${mycollection_text}              我的播单
    element should contain text in time     xpath=${forum_text}                     官方论坛
    element should contain text in time     xpaht=${usehelp_text}                   使用帮助
    element should contain text in time     xpaht=${settingbutton_text}             设置
    element should contain text in time     xpaht=${about_text_left}                关于
    element should contain text in time     xpaht=${about_text_rigth}               加入官方粉丝群



