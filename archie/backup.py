import os
import tarfile
from contextlib import closing
from . import helpers

def gzip_then_store(filename, backupdir):
    fname = os.path.basename(filename)
    archivename = os.path.join(backupdir, '%s.tgz' % fname)
    with closing(tarfile.open(archivename, 'w:gz')) as tar:
        tar.add(filename)
    helpers.add_checksum(archivename)
    return archivename

def Backup(cfg, rcfiles):
    backupfiles = []
    backupdir = cfg.get('dirs', 'backup-dir')
    helpers.ensure_dir_exists(backupdir)
    for rc in rcfiles:
        orifile = helpers.get_rcfile(cfg, rc)
        if os.path.lexists(orifile) and not os.path.islink(orifile):
           backupfiles.append(gzip_then_store(orifile, backupdir))
    return backupfiles
