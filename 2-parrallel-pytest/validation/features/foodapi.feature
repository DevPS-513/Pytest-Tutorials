@food
Feature: Food API validation

@TEST_1 @parallel_safe
Scenario: Verify that the food API returns a valid response for a given food item
    Given the food API endpoint is available
    When I send a GET request to the food API with the food item "apple"
    Then the response status code should be 200
    And the response body should contain the food item "apple"

@TEST_2 @parallel_safe
Scenario: Verify that the food API returns a valid response for a given food item with special characters
    Given the food API endpoint is available
    When I send a GET request to the food API with the food item "spaghetti & meatballs"
    Then the response status code should be 200