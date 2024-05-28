*** Settings ***
Library  SeleniumLibrary


*** Variables ***

*** Test Cases ***
Verify Frames
    Open Browser   https://jqueryui.com/checkboxradio/  Chrome
    Wait Until Element Is Visible    xpath://body/div[@id='container']/div[@id='logo-events']/h2[1]/a[1]      timeout=5
    Select Frame    xpath://iframe[@class='demo-frame']
    Sleep    4s
    Click Element    xpath://label[normalize-space()='New York']