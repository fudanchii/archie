===========
archie
===========

Archie manage your symlink.

Mostly purposed to manage config and rc files.


How To Use:
-----------

Usage:
    arc (install | restore) [--backup-dir=<backup-dir>] [--config=<config>] [--target=<target>] PACKAGE

    arc (-h | --help)

    arc (-v | --version)

Options:
    -b <backup-dir>, --backup-dir=<backup-dir>  Use this directory to store backup file.
                                                (override 'backup-dir' from config file)
    -c <config>, --config=<config>              Configuration file to use.
                                                (default is <PACKAGE>/a.rc)
    -h, --help                                  Show this help.
    -t <target>, --target=<target>              Target directory to install to.
                                                (default is /tmp)
    -v, --version                               Show program version.


a.rc file
---------
By default, archie uses a.rc file found in the `PACKAGE` folder.

This file can be overriden by specifying arguments to arc.

a.rc has 2 sections:

- dirs
    Contains 'target' and 'backup-dir'

- rcfiles
    List of config files to be installed.

License
-------
MIT License

Nurahmadie <nurahmadie@gmail.com>

Current status:


.. image:: https://travis-ci.org/fudanchii/archie.png?branch=master
    :target: https://travis-ci.org/fudanchii/archie

