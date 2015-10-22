import yaml
import os
from nose.tools import *
from nc.taskrunner import *
from nc.config import parse_config


full_path = os.path.dirname((os.path.realpath(__file__)))
good_config = yaml.load(
    file(
        full_path + "/test_good_config.yaml", 'r'
    )
)
bad_config = yaml.load(
    file(
        full_path + "/test_bad_config.yaml", 'r'
    )
)

class TestTaskRunner:

    def setup(self):
        print("setting up test of task runner class")
        self.config = parse_config(good_config)

    def teardown(self):
        print("tearing down test of task runner class")

    # def test_good__init__(self):
        # tr = TaskRunner(commands=good_config["commands"], devices=good_config["devices"])
