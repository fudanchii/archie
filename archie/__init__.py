import os
from .configuration import Config
from . import handlers as cmd


VERSION = '0.0.1'
APPNAME = 'archie'


def main(args):
    configfile = args['--config'] or os.path.join(args['PACKAGE'], 'a.rc')
    cfg = Config(configfile, args)

    if args['install']:
        cmd.Install(cfg)
    elif args['restore']:
        cmd.Restore(cfg)
