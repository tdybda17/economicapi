class Listener:
    response = None

    def on_success(self):
        raise NotImplementedError()
