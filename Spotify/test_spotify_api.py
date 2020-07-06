import json
import requests

# pytest

class TestClass:

    def test_given_valid_url_check_status_code_equals_200(self):
        response = requests.get("https://api.spotify.com")
        assert response.status_code == 200

    def test_get_current_user_check_status_code_equals_200(self):
        url = 'https://api.spotify.com/v1/me'
        user_ID = 'miq9x438ysuedi1io43rz0awv'
        headers = {
            'authorization': 'Bearer BQCNRDdTq1EgEJkH9oIdcInM1po64Ytw0QfCVu3FyiHRqBun-_qJlSxmlM_Cnw7K_bMzJL5XNEo1MoI6vqnUx9XjmWCisnY5KwlI0PgcvIP61OSJgXw41vhiTjGUYhQISRxkdjKbYxW003yj0Flb2ZwjrIH1U_qmlnJs3lGzJd89DzAH_E0si7rkTn8VasGbvDGU2RBiL7VJdBH6wCBQcc9aStxudCKGdiZygd6hXWOs7O8P4w30takWDww5ITGt-X3o5yArTS82iJU-_WrCZH53Wz_6kQVF',
            'cache-control': 'no-cache'
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

        json_response = response.json()
        print(json_response)

        data = json.load(response.content, 'id')
        assert data['id'] == user_ID

    def test_get_current_user_playlist_check_status_code_equals_200(self):
        url = 'https://api.spotify.com/v1/me/playlist'
        headers = {
            'authorization': 'Bearer BQCNRDdTq1EgEJkH9oIdcInM1po64Ytw0QfCVu3FyiHRqBun-_qJlSxmlM_Cnw7K_bMzJL5XNEo1MoI6vqnUx9XjmWCisnY5KwlI0PgcvIP61OSJgXw41vhiTjGUYhQISRxkdjKbYxW003yj0Flb2ZwjrIH1U_qmlnJs3lGzJd89DzAH_E0si7rkTn8VasGbvDGU2RBiL7VJdBH6wCBQcc9aStxudCKGdiZygd6hXWOs7O8P4w30takWDww5ITGt-X3o5yArTS82iJU-_WrCZH53Wz_6kQVF',
            'cache-control': 'no-cache'
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
