#Test case 10
#Initiating the claim request and validating the claim request is listed in the users claim history
Feature: Claim functionality
  Scenario: Initiate a claim request

    Given I open the login page
    And I login with valid username and valid password
    When I navigate to claim section
    And I click on submit claim
    And I fill on required fields
    And I click on create button
    Then success message has to displayed
    And the request should be listed in users claim history

