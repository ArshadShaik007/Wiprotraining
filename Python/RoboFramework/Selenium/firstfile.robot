*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    loginToapplication
    close browser

*** Keywords ***
loginToapplication
    maximize browser window
    Sleep  4s
    input text  xpath://input[@name='username']   Admin
    input text  xpath://input[@name='password']   admin123
    Sleep  4s
    click Element   xpath://button[@type='submit']
    Sleep  2s