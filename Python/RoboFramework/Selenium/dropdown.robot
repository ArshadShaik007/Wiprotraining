*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://the-internet.herokuapp.com/dropdown

*** Test Cases ***
RadioButton
        open browser        ${url}    ${browser}
        maximize browser window
        Sleep   4s
        wait until element is visible        id:dropdown     timeout=8
        Sleep   2s
        select from list by index       id:dropdown     1
        Sleep   2s
        select from list by value       id:dropdown     2
        Sleep   2s
        list selection should be    id:dropdown  Option 2