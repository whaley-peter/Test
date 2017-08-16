*** Settings ***
Library     libs/AppiumExtend.py
Variables       eles/globaleles.py
Suite Setup         switch to debug mode
Suite Teardown         back to homepage
Force Tags      localmanagent