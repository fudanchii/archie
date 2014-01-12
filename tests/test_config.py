import os, archie, pytest

from fixtures import args

@pytest.fixture
def args_pkg():
    myargs = args.copy()
    myargs['install'] = True
    myargs['PACKAGE'] = 'tests/rc'
    return myargs

@pytest.fixture
def args_args():
    myargs = args.copy()
    myargs['install']  = True
    myargs['PACKAGE']  = 'tests/rc'
    myargs['--config'] = 'tests/rc/a.rc'
    return myargs

class TestConfig:
    def test_configfile_from_package(self, args_pkg):
        cfg = archie.configuration.Config(os.path.join(args_pkg['PACKAGE'], 'a.rc'), args_pkg)
        self.do_assertions(cfg)

    def test_configfile_from_args(self, args_args):
        cfg = archie.configuration.Config(args_args['--config'], args_args)
        self.do_assertions(cfg)

    def do_assertions(self, cfg):
        assert 'dirs' in cfg.conf.sections()
        assert 'target' in cfg.options('dirs')
        assert cfg.get('dirs', 'target') == '/tmp/test'
        assert cfg.get('dirs', 'backup-dir') == '/tmp/test/.rc-backup'
