*** Settings ***
Library     libs/AppiumExtend.py
Suite Setup     login and swith to debug mode   ${False}
Suite Teardown    back to homepage
Force Tags      shipinxiangqingye