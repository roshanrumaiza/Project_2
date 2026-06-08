#Test case 5
  #creating new user and validating login with the newly created credentials
Feature: New user creation
  Scenario: creating a new user and validating login with newly created credentials
    Given I open the login page
    And I login with valid username and valid password
    When I click on admin
    And I click on add button
    And I enter the user details
    And I click on save button
    Then I should get the success message
    When I click on logout button
    And I login with the newly created credentials
    Then I should redirected to the homepage

  #Test case 6:
  #validating the presence of newly created user listed is the user list
  Scenario: Validate presence of the newly created user in the admin user list
    Given I open the login page
    And I login with valid username and valid password
    When I click on admin
    And I click on user management
    And I click on users
    Then newly created user should be present in the user list
































