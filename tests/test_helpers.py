import os, \
  archie, pytest, shutil

from fixtures import args

@pytest.fixture(scope="function")
def dir_name(request):
    dirname = '/tmp/tests/yay'
    def teardown():
        shutil.rmtree('/tmp/tests')
    request.addfinalizer(teardown)
    return dirname

@pytest.fixture
def config():
    myargs = args.copy()
    myargs['PACKAGE'] = 'tests/rc'
    cfg = archie.configuration.Config('tests/rc/a.rc', myargs)
    return cfg

class TestHelper:
    def test_ensure_dir_exists(self, dir_name):
        archie.helpers.ensure_dir_exists(dir_name)
        assert os.path.lexists(dir_name)
        assert os.path.isdir(dir_name)

    def test_get_rcfile(self, config):
        getrc = archie.helpers.get_rcfile
        assert getrc(config, 'hgignore') == '/tmp/test/muhaha/.hgignore'
        assert getrc(config, 'bashrc') == '/tmp/test/.bashrc'
        assert getrc(config, 'vimrc') == '/tmp/test/another/dir/oyay'
