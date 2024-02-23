import os, \
    archie, pytest, shutil

from fixtures import args


def teardown():
    shutil.rmtree('/tmp/another', ignore_errors=True)
    shutil.rmtree('/tmp/backupdir', ignore_errors=True)

@pytest.fixture(scope='function')
def config(request):
    myargs = args.copy()
    myargs['PACKAGE'] = 'tests/rc'
    cfg  = archie.configuration.Config('tests/rc/another-config.rc', myargs)
    archie.helpers.ensure_dir_exists(cfg.get('dirs', 'target'))
    shutil.copy('tests/rc/a.rc', '/tmp/another/')
    request.addfinalizer(teardown)
    return cfg

class TestRestore:
    def test_restore(self, config):
        archie.cmd.Install(config)
        assert os.path.lexists('/tmp/another/a.rc')
        assert os.path.islink('/tmp/another/a.rc')

        assert os.path.lexists('/tmp/backupdir/tests_rc-a.rc.tgz')

        archie.cmd.Restore(config)
        assert os.path.lexists('/tmp/another/a.rc')
        assert not os.path.islink('/tmp/another/a.rc')
