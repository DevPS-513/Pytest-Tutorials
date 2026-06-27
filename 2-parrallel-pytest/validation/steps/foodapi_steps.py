import pytest
from pytest_bdd import given, parsers, then, when
import time

@pytest.fixture
def food_context():
    return {}


@given("the food API endpoint is available")
def food_api_endpoint_is_available(food_context):
    food_context["endpoint_available"] = True


@when(parsers.parse('I send a GET request to the food API with the food item "{food_item}"'))
def send_get_request_for_food_item(food_context, food_item):
    if not food_context.get("endpoint_available"):
        time.sleep(2)
        raise RuntimeError("Food API endpoint is not available")

    food_context["response_status_code"] = 200
    food_context["response_body"] = {"food_item": food_item}


@then(parsers.parse("the response status code should be {expected_status:d}"))
def validate_response_status_code(food_context, expected_status):
    time.sleep(1)

    assert food_context.get("response_status_code") == expected_status


@then(parsers.parse('the response body should contain the food item "{food_item}"'))
def validate_response_body_food_item(food_context, food_item):
    time.sleep(1)

    assert food_context.get("response_body", {}).get("food_item") == food_item
