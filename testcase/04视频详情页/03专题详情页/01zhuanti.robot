*** Settings ***
Library              libs/AppiumExtend.py
Variables            eles/homepage.py
Variables            eles/videodetailspage.py
Suite Setup          back to homepage
Suite Teardown       swipe nth back to jingxuan tab
#Test Setup           kill logcat         ${udid}
#Test Teardown        run keyword if test failed       logcat     ${udid}     zhuanti
Force Tags           zhuanti

*** Test Cases ***
从自动化测试tab跳转到专题内--testzhuanti001
    wait until element is visible               id=${homebase}              15
    click nth element until no error            id=${homebase}
    swipe left nth
    nth element should contain text in time     id=${label_recommends}      蒙面唱将--手动编排
    click nth element                           id=${label_recommends}
    nth element should contain text in time     id=${topic_name}            蒙面唱将第二期       1

检查专题页面元素--testzhuanti002
    element should contain text in time         id=${topic_video_num}                  6个视频
    element should contain text in time         id=${topic_decription}                 在《蒙面唱将猜猜猜》第二期节目中
#滑动界面到专题底部
    swipe up nth        4
    element should contain text in time         xpath=${topic_name_in_titlebar}        蒙面唱将第二期

分享专题--testzhuanti003
    element should contain text in time         id=${topic_share_to_title}             分享专题至
    element should contain text in time         xpath=${topic share sina}              新浪微博
    element should contain text in time         xpath=${topic share weixin}            微信
    element should contain text in time         xpath=${topic share weixinfriends}     朋友圈
    element should contain text in time         xpath=${topic share qq}                QQ好友
    element should contain text in time         xpath=${topic share qqzone}            QQ空间
#    share test                                 蒙面唱将第二期

播放专题最后一个视频--testzhuanti004
    nth element should contain text             id=${videos_name_in_topic}      蒙面唱将第二期：女帝驯鹿铁皮人    -1
    click nth element until no error            id=${videos_name_in_topic}      -1
    sleep               5
    element should contain text in time         id=${videoname}                 蒙面唱将第二期：女帝驯鹿铁皮人
    go back
    swipe down nth      4

播放整个专题--testzhuanti004
    click element until no error                id=${topic_play}
    element should contain text in time         id=${video name in topic play}      蒙面唱将第二期：铁皮人
    click back nth      2
