*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/search.py
Variables   eles/globaleles.py
Suite Teardown       back to homepage

*** Test Cases ***
搜索功能1--testsearch001
        [Documentation]  检查界面及是否可正常输入删除
        click element       id=${homepage}
        click element       id=${search}
#检查界面
        element should contain text     id=${etsearch}     搜索全部视频内容
#检查是否可正常输入和删除
        input text          id=${etsearch}        lutaitai
        element should contain text     id=${etsearch}     lutaitai
        clear text          id=${etsearch}
        element should contain text     id=${etsearch}     搜索全部视频内容
#搜索不到对应内容
        input text          id=${etsearch}        dangshizhidaoshixunchang
        click element       id=${tvsearch}
        page should contain element      id=${imgempty}
        element should contain text      id=${tvempty}     抱歉，未找到相关视频
#取消
        click element       id=${quxiao}
搜索功能2--testsearch002
        [Documentation]  检查搜索的视频及清空搜索历史操作
#搜索视频并点击观看
        click element       id=${search}
        input text          id=${etsearch}        jhh
        click element       id=${tvsearch}
        ${tvname1}       get nth element text    id=${tvname}   2
        click nth element   id=${pic}         2
#检查播放视频
        wait until element is visible         id=${programname}
        ${tvname2}          get text          id=${programname}
        should be equal     ${tvname1}        ${tvname2}

        go back
        click element   id=${quxiao}
#清空搜索历史
        click element   id=${search}
        click element   id=${searchdelete}
        click element   id=${quxiao}
        click element   id=${search}
        page should not contain element      id=${ivpic}
