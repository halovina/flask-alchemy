from application import create_app, db
from application import models
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run()