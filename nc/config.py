

def parse_config(config):
    parsed_config = {}
    for conf, val in config.iteritems():
        if type(conf) != str:
            raise AssertionError("Expecting string for command %s" % (conf))
        if type(val) != list:
            raise AssertionError("Expecting list for value list %s" % (val))
        for vv in val:
            if type(vv) != str:
                raise AssertionError("Expecting string for command %s: %s" % (val, vv))
        parsed_config[conf] = val
    return parsed_config
