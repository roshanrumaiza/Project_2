#Test case 8
#validating the presence of menu items under My info
Feature:My info validation
  Scenario: Validate the  presence of menu items under “My Info”
    Given  I open the login page
    And I login with valid username and valid password
    When I click on My info
    Then menu items under My info should be visible and clickable
