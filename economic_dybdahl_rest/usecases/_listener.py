class Listener:
    response = None

    def on_success(self):
        raise NotImplementedError()

    def get_response(self):
        return self.response
