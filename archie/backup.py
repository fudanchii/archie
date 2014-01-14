import os
import tarfile
from contextlib import closing
from . import helpers

def gzip_then_store(filename, archivename):
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
            fname = os.path.basename(orifile)
            archivename = os.path.join(backupdir, \
                '%s-%s.tgz' % (cfg.get('args', 'PACKAGE').replace('/', '_'), fname))
            backupfiles.append(gzip_then_store(orifile, archivename))
    return backupfiles
