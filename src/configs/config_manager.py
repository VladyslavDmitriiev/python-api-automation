import json
from src.main.api import ApiClient


class Config:

    def __init__(self, file_name):
        self.file_name = file_name
        self.token = None

        self.config_dict = self._parse_file()

        # url
        self.hostname = self.config_dict["url"]["hostname"]
        # auth
        self.auth_path = self.config_dict["auth"]["path"]
        self.auth_headers = self.config_dict["auth"]["headers"]
        self.auth_data = self.config_dict["auth"]["data"]
        # ping
        self.ping_path = self.config_dict["ping"]["path"]

    def _parse_file(self) -> dict:
        with open(f"src/configs/{self.file_name}", "r") as c:
            config_dict = json.loads(c.read())
            return config_dict

    def get_token(self):
        path = self.config_dict["url"]["auth_path"]
        headers = self.config_dict["auth"]["headers"]
        data = self.config_dict["auth"]["data"]

        response = ApiClient.post(path, headers=self.auth_headers, data=self.auth_data)
        response_text = json.loads(response.text)
        self.token = response_text["token"]
        return self.token
