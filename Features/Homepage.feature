##Test case 4
#validating the functionalities of main menu items after login
Feature:Validation of Main menu functionality
  Scenario: validation of visibility and accessibility of main menu items after login
    Given I open the login page
    When I login with valid username and valid password
    And I click Login button
    Then I am  redirected to the homepage
    And Main menu items such as Admin,PIM,Leave,Time,Recruitment,My info,Performance,Dashboard should be visible and clickable
