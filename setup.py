#! /usr/bin/env python

from distutils.core import setup
from archie import APPNAME, VERSION

setup(
    name         = APPNAME,
    version      = VERSION,
    description  = 'Symlink management for configuration (rc) file.',
    author       = 'Nurahmadie',
    author_email = 'nurahmadie@gmail.com',
    url          = 'http://bitbucket.org/fudanchii/archie',
    packages     = ['archie', 'archie.handlers'],
    scripts      = ['arc']
    )
