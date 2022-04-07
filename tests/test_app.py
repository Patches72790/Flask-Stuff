

def test_app(app, client):
    client.get('/fun_stuff')
    assert True is False
