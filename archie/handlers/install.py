import os, shutil
from archie import helpers, backup

def create_symlink(cfg, pkg, rcfiles):
    for rc in rcfiles:
        ourfile = os.path.abspath(os.path.join(pkg, rc))
        orifile = helpers.get_rcfile(cfg, rc)
        if os.path.lexists(orifile):
            try:
                os.unlink(orifile)
            except OSError:
                if os.path.isdir(orifile):
                    shutil.rmtree(orifile)
        else:
            helpers.ensure_dir_exists(os.path.dirname(orifile))
        os.symlink(ourfile, orifile)

def Install(cfg):
    pkg = cfg.get('args', 'PACKAGE')
    rcfiles = cfg.options('rcfiles')
    helpers.ensure_dir_exists(cfg.get('dirs', 'target'))
    backup.Backup(cfg, rcfiles)
    create_symlink(cfg, pkg, rcfiles)
