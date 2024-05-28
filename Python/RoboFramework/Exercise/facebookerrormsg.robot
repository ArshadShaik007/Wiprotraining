*** Settings ***
Library  SeleniumLibrary
*** Variables ***
*** Test Cases ***
Verify screenshot
    Open Browser   https://facebook.com/login      Chrome
    Sleep  2s
    click element   xpath://button[@id='loginbutton']
    Sleep  2s
    Element Text Should Be  (//div[normalize-space()='Invalid username or password'])[1]   Invalid username or password
    Sleep  3s
    Close Browser