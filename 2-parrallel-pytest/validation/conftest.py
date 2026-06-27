import os
import datetime
import pytest
pytest_plugins = [
	"validation.steps.foodapi_steps",
	"validation.steps.logs_steps",
]


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n>>> session_setup fixture called")


def pytest_collection_modifyitems(items):
    """Automatically group non-parallel_safe tests onto a single worker."""
    for item in items:
        if not item.get_closest_marker("parallel_safe"):
            item.add_marker(pytest.mark.xdist_group("serial"))