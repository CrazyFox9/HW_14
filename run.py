from flask import Flask
from views import movies_blueprint

app = Flask(__name__)

app.register_blueprint(movies_blueprint)
app.config['JSON_SORT_KEYS'] = False

if __name__ == '__main__':
    app.run(debug=True)
