*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
VerifyWaits
    open browser    https://the-internet.herokuapp.com/checkboxes      Chrome
    Sleep  4s
    Wait Until Element Is Visible   xpath://h3[normalize-space()='Checkboxes']   timeout=5
    Wait Until Element Is Visible   xpath:(//input[@type='checkbox'])[1]