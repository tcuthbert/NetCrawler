import yaml
import os
from nose.tools import *
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


def test_good_load_config():
    print parse_config(good_config)
    assert parse_config(good_config)


def test_bad_load_config():
    print parse_config(bad_config)
    assert_raises(AssertionError, parse_config, bad_config)
