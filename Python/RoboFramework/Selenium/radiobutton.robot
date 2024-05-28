*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://the-internet.herokuapp.com/checkboxes

*** Test Cases ***
RadioButton
    open browser    ${url}  ${browser}
    maximize browser window
    Sleep  4s
    click Element   xpath:(//input[@type='checkbox'])[1]
    sleep  2s
    click Element   xpath:(//input[@type='checkbox'])[2]