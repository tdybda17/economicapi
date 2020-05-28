import json


class Model:

    def to_dict(self):
        raise NotImplementedError()

    @staticmethod
    def from_dict(_dict):
        raise NotImplementedError()

    def to_json(self):
        return json.dumps(self.to_dict())
