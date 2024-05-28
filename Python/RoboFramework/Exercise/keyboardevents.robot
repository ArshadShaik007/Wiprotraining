*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
Verify Keyboard Events
    open browser    https://the-internet.herokuapp.com/key_presses      Chrome
    Wait Until Element Is Visible   //h3[normalize-space()='Key Presses']   timeout=5
    Sleep  3s
    Press Keys  id:target       SPACE
    Sleep  3s
    Press Keys  id:target       TAB
    Sleep  3s
    Press Keys  id:target       SHIFT
    Sleep  3s