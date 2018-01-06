import sanic
import json
import zlib


async def test_simple(app, client, raven_send_remote):

    @app.route('/test')
    def simple(_):
        return sanic.response.text('text')

    response = await client.get('/test')
    assert response.status == 200
    response_text = await response.text()
    assert response_text == 'text'
    raven_send_remote.assert_not_called()


async def test_exception(app, client, raven_send_remote):
    @app.route('/test')
    def simple(request):
        raise ValueError("test")

    response = await client.get('/test')
    assert response.status == 500

    assert raven_send_remote.call_count == 1
    data = json.loads(zlib.decompress(raven_send_remote.call_args_list[0][1]['data']).decode("utf-8"))
    assert set(data['extra'].keys()) == {'sys.argv', 'url', 'method', 'headers', 'body', 'query_string'}
    assert data['exception']['values'][0]['value'] == 'test'
    assert data['exception']['values'][0]['type'] == 'ValueError'



