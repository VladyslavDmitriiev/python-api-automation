import pytest
import allure


@allure.feature("Authorization")
@allure.story("User authorize and receive a token")
class TestAuthCreateToken:
    def test_response_status_code(self, api):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=api.config.auth_headers, data=api.config.auth_data)

        with allure.step("Check response status code"):
            assert 200 == response.status_code, f"Invalid response status code {response.status_code}"

    def test_json_in_response(self, api):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=api.config.auth_headers, data=api.config.auth_data)

        with allure.step("Check if response text in json format"):
            assert api.is_json(response.text), f"Response text isn't json {response.text}"

        with allure.step("Check if the response contains a correct token length"):
            response_text = api.json_to_dict(response.text)
            token_len = len(response_text["token"])
            assert 15 == token_len, f"Wrong token length {token_len}"


@allure.feature("Authorization")
@allure.story("User uses an invalid header to authorize")
@pytest.mark.parametrize("invalid_headers",    [{"invalid": "invalid"},
                                                {"Content-Type": "invalid"},
                                                {"invalid": "application/json"}])
class TestAuthInvalidHeaders:
    def test_response_status_code(self, api, invalid_headers):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=invalid_headers, data=api.config.auth_data)

        with allure.step("Check response status code"):
            assert 401 == response.status_code

    def test_json_in_response(self, api, invalid_headers):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=invalid_headers, data=api.config.auth_data)

        with allure.step("Check if response text in json format"):
            assert api.is_json(response.text)

        with allure.step("Check if the response contains a correct reason"):
            response_text = api.json_to_dict(response.text)
            assert "Bad credentials" == response_text["reason"]


@allure.feature("Authorization")
@allure.story("User uses an invalid data (username, password) to authorize")
@pytest.mark.parametrize("invalid_data",   [{"username": "invalid", "password": "invalid"},
                                            {"username": "admin", "password": "invalid"},
                                            {"username": "invalid", "password": "password123"}])
class TestAuthInvalidData:
    def test_response_status_code(self, api, invalid_data):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=api.config.auth_headers, data=invalid_data)

        with allure.step("Check response status code"):
            assert 401 == response.status_code

    def test_json_in_response(self, api, invalid_data):
        with allure.step("Send POST request"):
            response = api.post(api.config.auth_path, headers=api.config.auth_headers, data=invalid_data)

        with allure.step("Check if response text in json format"):
            assert api.is_json(response.text)

        with allure.step("Check if the response contains a correct reason"):
            response_json = api.json_to_dict(response.text)
            assert "Bad credentials" == response_json["reason"]