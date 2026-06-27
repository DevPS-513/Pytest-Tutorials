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
    file_path = os.path.join(os.path.dirname(__file__), datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".txt")
    with open(file_path, 'w') as file:
        file.write("now")
    print(f">>> log file created: {file_path}")