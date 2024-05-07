*** Settings ***
Documentation    File which has all the locators Info
Library    SeleniumLibrary

#Contains all the locator information

*** Variables ***
${loc_id}          id:userEmail
${loc_pwd}      id:userPassword
${loc_Button}        id:login
${sign_out}    xpath://button[normalize-space()='Sign Out']
${login_confirmation}    css:div[class='left mt-1'] h3
${logout_confirmation}    css:.login-title

