import os, \
    archie, pytest, shutil

from fixtures import args

@pytest.fixture(scope='function')
def config(request):
    myargs = args.copy()
    myargs['PACKAGE'] = 'tests/rc'
    cfg = archie.configuration.Config('tests/rc/another-config.rc', myargs)
    def teardown():
        shutil.rmtree(cfg.get('dirs','target'))
        shutil.rmtree(cfg.get('dirs', 'backup-dir'))
    request.addfinalizer(teardown)
    return cfg

class TestInstall:
    def test_install(self, config):
        archie.cmd.Install(config)
        assert os.path.lexists('/tmp/another/a.rc')
        assert os.path.islink('/tmp/another/a.rc')
