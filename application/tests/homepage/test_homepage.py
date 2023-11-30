

def test_homepage(tclient):
    response = tclient.get('/')
    assert response.status_code == 200