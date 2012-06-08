import os

import flask


class Application(flask.Flask):
    """I am the core flask application."""

    def __init__(self, config_envvar='APP_CONFIG'):
        flask.Flask.__init__(self, __package__)
        self.config['HOST'] = os.environ.get('HOST', '0.0.0.0')
        self.config['PORT'] = int(os.environ.get('PORT', '5000'))
        self.config['DEBUG'] = bool(os.environ.get('DEBUG'))
        self.config['SECRET_KEY'] = os.urandom(24)
        self.config.from_envvar(config_envvar, silent=True)

    def run(self, *args, **kwds):
        kwds.setdefault('debug', self.config['DEBUG'])
        kwds.setdefault('port', self.config['PORT'])
        kwds.setdefault('host', self.config['HOST'])
        flask.Flask.run(self, *args, **kwds)


def create_application(*args, **kwds):
    app = Application(*args, **kwds)

    @app.route('/')
    def index():
        return 'Hi There'

    return app

