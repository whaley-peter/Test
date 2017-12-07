*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/search.py
Variables   eles/globaleles.py
Variables   eles/videodetailspage.py
Suite Setup     login and switch to debug mode
Suite Teardown       back to homepage
Force Tags      search

*** Test Cases ***
跳转到搜索界面和回到主界面----testsearch001
    click element until no error    id=${homepage}
    element should contain text in time     id=${homepage_search_text}     搜索
    click element until no error            id=${homepage_search}
#如果存在搜索历史，则清空
    ${val}  is element present              id=${search_history_delete}
    run keyword if      ${val}      click element until no error    id=${search_history_delete}
    element should contain text in time     id=${search_text}              搜索全部视频内容
    element should contain text in time     id=${quxiao}                   取消
    click element until no error            id=${quxiao}
    element should contain text in time     id=${homepage_search_text}     搜索

搜索内容为空----testsearch002
    click element until no error            id=${homepage_search}
    input text     id=${search_input}       dangshizhidaoshixunchang
    element should contain text in time     id=${searchbutton_text}           搜索
    click element until no error            id=${searchbutton}
    page should contain element             id=${search_empty_pic}
    element should contain text in time     id=${search_empty_text}     抱歉，未找到相关视频

搜索全景视频----testsearch003
    input text      id=${search_input}       JHH视频3
    click element until no error             id=${searchbutton}
    ${name}         get text                 id=${searched_video_name}
    page should contain element              id={searched_video_pic}
    click element until no error             id=${searched_video_name}
    ${name_in_detail_page}      get text     id=${videoname}
    should be equal             ${name}      ${name_in_detail_page}
    page should contain element              id=${downloadbutton}
    click element until no error             id=${downloadbutton}
    element should contain text in time      xpath=${downloadtext}      已缓存
    page should contain element              id=${addtocollection}
    page should contain element              id=${share}
    page should not contain element          id=${description}
    element should contain text in time      id=${postername}           微鲸VR
    element should contain text in time      id=${posterfollow}         关注
    click back nth

搜索3D电影----testsearch004
    input text      id=${search_input}       狄仁杰之神都龙王
    click element until no error             id=${searchbutton}
    ${name}         get text                 id=${searched_video_name}
    page should contain element              id=${searched_video_pic}
    click element until no error             id=${searched_video_name}
    ${name_in_detail_page}      get text     id=${videoname}
    should be equal             ${name}      ${name_in_detail_page}
    page should contain element              id=${downloadbutton}
    page should contain element              id=${addtocollection}
    element should contain text in time      id=${district_title}     地区
    element should contain text in time      id=${district}           内地
    element should contain text in time      id=${year_title}         年代
    element should contain text in time      id=${year}               2013
    element should contain text in time      id=${director_title}     导演
    element should contain text in time      id=${director}           徐克
    element should contain text in time      id=${actor_title}        主演
    element should contain text in time      id=${actor}              赵又廷;冯绍峰;林更新;杨颖
    element should contain text in time      id=${description}        21岁的狄仁杰前往大理寺报到任职时
    page should contain element              id=${share}
    page should not contain element          id=${postername}
    page should not contain element          id=${posterfollow}
    click back nth

搜索互动剧----testsearch005
    input text      id=${search_input}       互动剧4（勿动！！！）
    click element until no error            id=${searchbutton}
    ${name}         get text                 id=${searched_video_name}
    page should contain element              id={searched_video_pic}
    click element until no error             id=${searched_video_name}
    ${name_in_detail_page}      get text     id=${videoname}
    should be equal             ${name}      ${name_in_detail_page}
    page should contain element              id=${downloadbutton}
    click element until no error             id=${downloadbutton}
    element should contain text in time      xpath=${downloadtext}       缓存
    page should contain element              id=${addtocollection}
    page should contain element              id=${share}
    page should not contain element          id=${description}
    element should contain text in time      id=${postername}            微鲸VR
    element should contain text in time      id=${posterfollow}          关注
    wait until element is visible            id=${switch branch left}     20
    page should contain element              id=${switch branch middle}
    page should contain element              id=${switch branch right}
    click back nth

查看并清空搜索历史----testsearch006
    click element until no error            id=${quxiao}
    click element until no error            id=${homepage_search}
    element should contain text in time     xpath=${history_text}       互动剧4（勿动！！！）
    click element until no error            xpath=${history1}
    element should contain text in time     id=${searched video name}   互动剧4（勿动！！！）
    click element until no error            id=${quxiao}
    click element until no error            id=${homepage_search}
    click element until no error            id=${search_history_delete}
    page should not contain element         id=${search_history_delete_text}
    click element until no error            id=${quxiao}

