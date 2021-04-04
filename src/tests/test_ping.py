import pytest
import allure


@allure.feature("Ping API")
@allure.story("Check if API is running")
class TestIfApiIsRunning:
    def test_status_code(self, api):
        with allure.step("Send GET request"):
            response = api.get(path=api.config.ping_path)
            # ToDo json file attaching
            # allure.png.attach.file(response.text, "response.text", allure.png.attachment_type.TEXT)

        with allure.step("Check status code"):
            assert 200 == response.status_code

    def test_response_text(self, api):
        with allure.step("Send GET request"):
            response = api.get(path=api.config.ping_path)
        with allure.step(f"Check response text"):
            assert "Created" == response.text
