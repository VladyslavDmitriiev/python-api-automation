import requests
import json


class ApiClient:
    def __init__(self, config):
        self.config = config
        self.hostname = config.hostname

    def get(self, path="/", params=None, headers=None, timeout=10):
        url = f"{self.hostname}{path}"
        return requests.get(url=url, params=params, headers=headers, timeout=timeout)

    def post(self, path="/", params=None, data=None, headers=None, timeout=10):
        url = f"{self.hostname}{path}"
        json_data = json.dumps(data)
        return requests.post(url=url, params=params, data=json_data, headers=headers, timeout=timeout)

    @staticmethod
    def is_json(text):
        try:
            json_object = json.loads(text)
        except ValueError as e:
            return False
        return True

    def json_to_dict(self, text):
        return json.loads(text) if self.is_json(text) else None
