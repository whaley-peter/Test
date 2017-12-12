*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/homepage.py
Variables   eles/videodetailspage.py
Suite Setup         back to homepage
Suite Teardown      back to homepage
Force Tags          jiemubao

*** Test Cases ***
从支付tab banner跳转到节目包内--testjiemubao001
    wait until element is visible               id=${homebase}              10
    click nth element until no error            id=${homebase}
    swipe left nth          4
    nth element should contain text in time     id=${name_in_banner}        pl节目包0703-3
    click nth element                           id=${name_in_banner}
    nth element should contain text in time     id=${topic_name}            pl节目包0703-3       1

检查节目包页面元素--testjiemubao002
    element should contain text in time         id=${topic_video_num}                  5个视频
    page should not contain element             id=${topic_decription}
#滑动界面到节目包底部
    swipe up nth        3
    element should contain text in time         xpath=${topic_name_in_titlebar}        pl节目包0703-3

分享节目包--testjiemubao003
    element should contain text in time         id=${topic_share_to_title}             分享节目包至
    element should contain text in time         xpath=${topic share sina}              新浪微博
    element should contain text in time         xpath=${topic share weixin}            微信
    element should contain text in time         xpath=${topic share weixinfriends}     朋友圈
    element should contain text in time         xpath=${topic share qq}                QQ好友
    element should contain text in time         xpath=${topic share qqzone}            QQ空间
#    share test                                  pl节目包0703-3


