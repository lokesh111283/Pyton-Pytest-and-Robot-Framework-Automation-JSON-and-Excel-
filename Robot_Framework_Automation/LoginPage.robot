*** Settings ***
Documentation   To validate the Login form
Library     SeleniumLibrary
Library    Collections
Resource    PathInfo.robot
Resource    DriverURLInfo.robot
Resource    LogoutPage.robot

*** Variables ***

#Below test case retrives the data from Logindata file and verifies the post to Login and Logout
*** Keywords ***
LoginPage.validate the Login
    [Arguments]    ${username}    ${password}
    DriverURLInfo.open the browser
    LoginPage.Login to WebPage    ${loc_id}    ${loc_pwd}    ${loc_Button}    ${username}    ${password}
    verify if login completed
    LogoutPage.Logout from WebPage
    LogoutPage.Verify if logout Completed
    DriverURLInfo.Close the Login Browser

LoginPage.Login to WebPage
    [Arguments]    ${loc_id}    ${loc_pwd}    ${loc_Button}    ${username}    ${password}
    Input Text    ${loc_id}    ${username}
    Input Password    ${loc_pwd}    ${password}
    Click Button    ${loc_Button}

verify if login completed
    ${logintext}    Get Text    ${login_confirmation}
    Log    ${logintext}
    Should Be Equal As Strings     ${logintext}     AUTOMATION