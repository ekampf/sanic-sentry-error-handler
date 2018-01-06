import pytest
import sanic
import sanic_sentry

@pytest.fixture(autouse=True)
def raven_send_remote(mocker):
    send_remote_mock = mocker.patch("raven.base.Client.send_remote")
    yield send_remote_mock


@pytest.fixture
def sentry_url():
    return 'http://public:secret@127.0.0.1:8000/1'


@pytest.yield_fixture
def app(sentry_url):
    app = sanic.Sanic("test_app")
    app.error_handler = sanic_sentry.SanicSentryErrorHandler(sentry_url)
    yield app

@pytest.fixture
def sanic_server(loop, app, test_server):
    return loop.run_until_complete(test_server(app))


@pytest.fixture
def client(loop, app, test_client):
    return loop.run_until_complete(test_client(app))
