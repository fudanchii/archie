import os, \
    archie, pytest, shutil

from fixtures import args

def setup_dir(targetdir, backupdir):
    def teardown():
        shutil.rmtree(backupdir)
        shutil.rmtree(targetdir)
    archie.helpers.ensure_dir_exists(targetdir)
    shutil.copy('tests/rc/a.rc', targetdir)
    return teardown

@pytest.fixture(scope='function')
def config(request):
    myargs = args.copy()
    myargs['PACKAGE'] = 'tests/rc'
    cfg = archie.configuration.Config('tests/rc/another-config.rc', myargs)
    request.addfinalizer( \
        setup_dir(cfg.get('dirs', 'target'), cfg.get('dirs', 'backup-dir')))
    return cfg

class TestBackup:
    def test_backup(self, config):
        assert os.path.lexists('/tmp/another') and os.path.isdir('/tmp/another')
        assert os.path.lexists('/tmp/another/a.rc') and os.path.isfile('/tmp/another/a.rc')

        rcfiles = config.options('rcfiles')
        assert len(rcfiles) == 1
        assert 'a.rc' in rcfiles
        assert archie.helpers.get_rcfile(config, 'a.rc') == '/tmp/another/a.rc'
        
        files = archie.backup.Backup(config, rcfiles)
        assert len(files) == 1
        assert os.path.lexists('/tmp/backupdir') and os.path.isdir('/tmp/backupdir')
        assert os.path.lexists('/tmp/backupdir/tests_rc-a.rc.tgz')
