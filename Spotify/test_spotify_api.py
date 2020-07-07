import json

import pytest
import requests


# pytest

class TestClass:

    @pytest.fixture
    def spotify_token(self):
        token = 'Bearer BQBa9rV6VmY1U9VNBLKsU3Ljy9ukQLjlTVUQiKB1zyNEAtVGOeUo5zZFJkoNo6Ctm2ng8NVgoy2nOR3GZF3w4eObXjHjpuYrPfqO-TDSsKWK9D1JU9fWf_CghXWXT7lHEQBFDhxrkpo0xvSoBNEY2s1Oy7N1LA69yT00YXREiWPiOTfD5mmEe4Er_QGNV5TqBM3HRBo3_vmBFQ0CsKntba6Lj_hQu-NvpL2SzH8clvj1zSViQwrUE-GfkDZkhlu9K9wrGcLLPJI9jbgFg3F-jxqgOe7EQTUW'
        headers = {
            'authorization': token,
            'cache-control': 'no-cache',
            'Content-Type': 'application/json'
        }
        return headers

    def test_given_valid_url_check_status_code_equals_200(self):
        response = requests.get("https://api.spotify.com")
        assert response.status_code == 200

    def test_get_current_user_check_status_code_equals_200(self, spotify_token):
        url = 'https://api.spotify.com/v1/me'
        response = requests.get(url, headers=spotify_token)
        assert response.status_code == 200
        response_body = response.json()
        global user_id
        user_id = response_body['id']
        assert user_id == 'miq9x438ysuedi1io43rz0awv'

    def test_creating_playlist_check_status_code_equals_200(self, spotify_token):
        global user_id
        total=5
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
        payload = {'name': 'BTS Songs', 'description': 'Playlist for BTS Songs', 'public': True}
        response = requests.post(url, headers=spotify_token, data=json.dumps(payload))
        createResponseBody = response.json()
        assert createResponseBody['name'] == 'BTS Songs' and response.status_code == 201
        print(json.dumps(createResponseBody))

    def test_get_current_user_playlist_check_status_code_equals_200(self, spotify_token):
        global user_id
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'

        response = requests.get(url, headers=spotify_token)
        assert response.status_code == 200
        getPlaylist_Response = response.json()
        total_playlist = getPlaylist_Response['total']
        assert total_playlist == 9
