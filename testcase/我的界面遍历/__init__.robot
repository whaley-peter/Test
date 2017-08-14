*** Settings ***
Library     libs/AppiumExtend.py
Variables       libs/cfg.py
Suite Setup     loginApp or not    ${False}
Force Tags      mypage
