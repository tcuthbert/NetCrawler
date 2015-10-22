import argparse
from nc.taskrunner import Discovery
from nc.config import parse_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cisco Network Discovery.')
    parser.add_argument('--config', dest='config_path', action='store',
                                        help='Path to configuration file')

    parser.add_argument("--devices", metavar="device-a.demo.local", type=str, nargs="+",
                      help="Device hostnames to run discovery against")

    args = parser.parse_args()
    config = parse_config(args.config_path)
    disco = Discovery(
        commands=config["commands"],
        devices=config["devices"]
    )
    disco.run()
    for dev, cmd in disco.results.items():
        print "Device: %s discovery information: " % dev
        for cmd, data in cmd.items():
            print cmd, data
