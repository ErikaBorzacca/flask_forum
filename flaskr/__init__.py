import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else :
        app.config.from_mapping(test_config)

    try :
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # db init
    from flaskr import db
    db.init_app(app)
    
    # init route for auth
    from flaskr import auth
    app.register_blueprint(auth.bp)

    # init route for blog
    from flaskr import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
