*** Settings ***
Library     libs/AppiumExtend.py
Suite Setup     login and switch to debug mode
Suite Teardown    back to homepage
Force Tags      mypage
