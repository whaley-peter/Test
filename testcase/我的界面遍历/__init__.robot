*** Settings ***
Library     libs/AppiumExtend.py
Variables       libs/cfg.py
Suite Setup     jump to homepage    ${False}
Force Tags      mypage
