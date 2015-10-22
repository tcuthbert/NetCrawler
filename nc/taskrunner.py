from trigger.cmds import Commando



class TaskRunner(Commando):
    commands = []
    
    def __init__(self, config, *args, **kwargs):
        self.commands = config["commands"]
        self.devices = config["devices"]
        super(TaskRunner, self).__init__()
