from trigger.cmds import Commando


class Runner(Commando):
    vendors = []
    commands = []


class Discovery(object):
    def __init__(self, *args, **kwargs):
        devices, vendors = zip(*map(lambda i: i.items()[0], kwargs["devices"]))
        runner = Runner
        runner.vendors = vendors
        runner.commands = kwargs["commands"]
        self._driver = Runner(devices=devices)

    def run(self):
        self._driver.run()

    @property
    def results(self):
        return self._driver.results
