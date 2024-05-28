*** Settings ***
Library  SeleniumLibrary
*** Variables ***
*** Test Cases ***
DatePicking
    Open Browser   https://jqueryui.com/datepicker      Chrome
    Sleep  3s
    Select Frame    xpath://iframe[@class='demo-frame']
    Sleep  2s
    Click Element   xpath://input[@id='datepicker']
    Sleep  2s
    Click Element   xpath://a[normalize-space()='28']
    Sleep  3s