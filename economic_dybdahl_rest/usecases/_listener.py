class Listener:
    response = None

    def on_success(self, data=None):
        raise NotImplementedError()

    def get_response(self):
        return self.response

    def on_unknown_error(self, status_code, content):
        raise NotImplementedError()

    def on_does_not_exist(self):
        raise NotImplementedError()
