@logs
Feature: Logging validation

@TEST_3 
Scenario: Verify that the food API returns a valid response for a given food item with special characters
    Given the food API endpoint is available
    When I send a GET request to the food API with the food item "spaghetti & meatballs"
    Then the response status code should be 200

@TEST_4 
Scenario: Verify that the food API returns a valid response for a given food item with special characters and spaces
    Given the food API endpoint is available
    When I send a GET request to the food API with the food item "chicken tikka masala"
    Then the response status code should be 200