*** Settings ***
Documentation   To validate the Login form
Library     SeleniumLibrary
Library    Collections
Library     DataDriver      file=Testdata.csv     encoding=utf_8   dialect=unix
Test Setup    DriverURLInfo.open the browser
Test Teardown    DriverURLInfo.Close the Login Browser
Test Template    LoginPage.Validate The Login
Resource    PathInfo.robot
Resource    DriverURLInfo.robot
Resource    LogoutPage.robot

*** Variables ***

#Below test case retrives the data from csv file mentioned in library and verifies the post to Login and Logout
*** Test Cases ***
Login with user ${username} and password ${password}        xyc@abc.com     123456

*** Keywords ***
LoginPage.validate the Login
    [Arguments]    ${username}    ${password}
    LoginPage.Login to WebPage    ${loc_id}    ${loc_pwd}    ${loc_Button}    ${username}    ${password}
    verify if login completed
    LogoutPage.Logout from WebPage
    LogoutPage.Verify if logout Completed

LoginPage.Login to WebPage
    [Arguments]    ${loc_id}    ${loc_pwd}    ${loc_Button}    ${username}    ${password}
    Input Text    ${loc_id}    ${username}
    Input Password    ${loc_pwd}    ${password}
    Click Button    ${loc_Button}

verify if login completed
    ${logintext}    Get Text    ${login_confirmation}
    Log    ${logintext}
    Should Be Equal As Strings     ${logintext}     AUTOMATION
