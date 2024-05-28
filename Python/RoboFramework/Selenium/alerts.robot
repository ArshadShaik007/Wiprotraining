*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://chercher.tech/practice/practice-pop-ups-selenium-webdriver

*** Test Cases ***
RadioButton
        open browser        ${url}    ${browser}
        maximize browser window
        Sleep   4s
        #SIMPLE ALERT
        click Element       xpath://input[@name='alert']
        Sleep  4s
        ${alert_msg} =      Handle Alert    action=ACCEPT     timeout=3
        Log To Console  ${alert_msg}
        #CONFIRMATION ALERT
        click Element       xpath://input[@name='confirmation']
        Sleep  4s
        ${alert_msg} =      Handle Alert    action=DISMISS     timeout=3
        Log To Console  ${alert_msg}