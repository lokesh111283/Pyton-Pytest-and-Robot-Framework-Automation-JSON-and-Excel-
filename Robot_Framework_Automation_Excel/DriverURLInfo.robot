*** Settings ***
Documentation    A Generic  file with reusable keywords and variables
Library    SeleniumLibrary

#contains the loginwebpage information and close browser method where it closes at the end
*** Variables ***
${url}    https://rahulshettyacademy.com/client

*** Keywords ***
DriverURLInfo.open the browser#contains the loginwebpage information and close browser method where it closes at the end
    Create Webdriver    Firefox   executable_path="E:\\Selenium3\\geckodriver.exe"
    Go To    ${url}

DriverURLInfo.Close the Login Browser
    Close Browser