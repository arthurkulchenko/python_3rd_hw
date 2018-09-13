'''
    Singleton Class that is holding in it self whole response objects for
    convenient passing it to wsgi app. That's give us separating wsgi app
    from its business logic.
'''

class Response:
    def __init__(self, status, headers, body, environment='development'):
        self.status = status
        self.headers = headers
        self.body = body
        self.environment = environment
