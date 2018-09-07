class Response:
    def __init__(self, status, headers, body, environment='development'):
        # super(Response, self).__init__()
        self.status = status
        self.headers = headers
        self.body = body
        self.environment = environment
