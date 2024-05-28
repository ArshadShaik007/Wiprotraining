*** Settings ***
Library  SeleniumLibrary

*** Variables ***

${browser}  chrome
${url}  https://rahulshettyacademy.com/seleniumPractise/#/

*** Test Cases ***
Add Button
    open browser    ${url}  ${browser}
    maximize browser window
    Sleep  2s
    click Element   xpath:(//div[@class='products']//div[1]//div[2]//a[2])
    Sleep  2s
    click Element   xpath:(//div[@class='products']//div[1]//div[3]//button[1])
    Sleep  2s
    click Element   xpath:(//img[@alt='Cart'])
    Sleep  2s
    click Element   xpath:(//button[normalize-space()='PROCEED TO CHECKOUT'])
    Sleep  2s
Placing Order
    click Element   xpath:(//button[normalize-space()='Place Order'])
    Sleep  2s
    wait until element is visible        tag:select     timeout=4
    Sleep   2s
    select from list by index       tag:select     88
    Sleep  2s
    list selection should be    tag:select  India
    Sleep  2s
    click Element   xpath:(//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/input[1])
    Sleep  2s
    click Element   xpath:(//button[contains(text(),'Proceed')])
    Sleep  4s
