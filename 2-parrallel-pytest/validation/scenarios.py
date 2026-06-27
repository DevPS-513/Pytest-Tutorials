from pytest_bdd import scenarios
import os

feature_path=os.path.join(os.path.dirname(__file__),"features")
scenarios(feature_path)