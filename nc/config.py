import yaml


def parse_config(configpath):
    config = yaml.load(
        file(
            configpath, 'r'
        )
    )
    parsed_config = {}
    for conf, val in config.iteritems():
        if type(conf) != str:
            raise AssertionError("Expecting string for command %s" % (conf))
        if type(val) != list:
            raise AssertionError("Expecting list for value list %s" % (val))
        for item in val:
            if item is None:
                raise AssertionError("Unexpected value in list %s" % (val))
        parsed_config[conf] = val
    return parsed_config
