import json

def test_get_userdata(tclient, init_mock_userdata):
    resp = tclient.get('/api/user/all')
    assert resp.status_code == 200
    
    resp_data  = json.loads(resp.data)
    assert resp_data['message'] == "success"
    assert len(resp_data['data']) == 2