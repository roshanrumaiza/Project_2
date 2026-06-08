Feature:Login functionality

Background:
  Given I open the login page

  #Test Case 2:
  #validating the Home url of orange website
  Scenario: Validate the URL of Orange HRM website
    Then I should be redirected to the loginpage

  #Test Case 3:
  #validating the visibility and click ability of login fields
  Scenario: Validate username and password field
    Then  Username and password field should be displayed and enabled


  #Test Case 1:
  #validating the login with the credentials from excel file
  Scenario: Login with the credentials from excel file
    When  I login with the credentials from excel file


#  Test case 4:
#validating the forgot password link is sent successfully to the registered email id
  Scenario: Validate forgot password link
    When  I click on forgot password link
    Then  I should get the popup to enter an email-id where password rest link will be sent
    And  I enter an email
    And  I click on submit button
    And I should get the message that the password link has been sent successfully to the registered email-id
