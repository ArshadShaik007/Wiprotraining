*** Settings ***
Documentation  File Upload Download in Robot Framework
Library  SeleniumLibrary
Library   OperatingSystem

*** Variables ***

*** Test Cases ***
Verify File Download
    [documentation]  This test case verifies that a user can successfully upload a file
    [tags]  Regression
    Open Browser  https://the-internet.herokuapp.com/download  Chrome
    Click Element  xpath://a[normalize-space()='selenium-snapshot.png']
    Sleep  3s
    ${files}    List Files In Directory    C:/Users/Public/Documents
    Length Should Be    ${files}    1
    Close Browser