*** Settings ***
Library     libs/AppiumExtend.py
Variables   eles/globaleles.py

Suite Setup     open application       ${remote server}     ${desired caps}
Suite Teardown  kill uiautomator
#指定变量${remote_url}、${udid}，分布式测试时，用于接收传入的变量
#Suite Setup     open mutilapplications       ${remote_url}       ${udid}
#Suite Teardown     kill uiautomators     ${udid}


Force Tags      testapp
