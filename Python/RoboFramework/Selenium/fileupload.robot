*** Settings ***
Documentation  File Upload Download in Robot Framework
Library  SeleniumLibrary
Library   OperatingSystem

*** Variables ***

*** Test Cases ***
Verify File Upload
    [documentation]  This test case verifies that a user can successfully upload a file
    [tags]  Regression
    Open Browser  https://the-internet.herokuapp.com/upload  Chrome
    Wait Until Element Is Visible  id:file-submit  timeout=5
    Choose File  id:file-upload  C:/Users/Public/Documents/Capture.png
    Click Element  id:file-submit
    Sleep  3s
    Element Text Should Be  tag:h3  File Uploaded!  timeout=5
    Element Text Should Be  id:uploaded-files  image.png  timeout=5