import json
import os

def test_get_userdata(tclient, init_mock_userdata):
    os.environ['CLIENT_APIKEY'] = '1233434345@122323SDSD'
    headers = {
        'client-api-key':'1233434345@122323SDSD'
    }
    
    resp = tclient.get('/api/user/all', headers=headers)
    assert resp.status_code == 200
    
    resp_data  = json.loads(resp.data)
    assert resp_data['message'] == "success"
    assert len(resp_data['data']) == 2