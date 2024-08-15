from flask import Flask

app = Flask(__name__, template_folder = "src/view/", static_folder = "public/")

from config.constants import *
from config.database import connect
from helper.helper import *
from migration.migration import migrate

db = connect(app)

if RUN_MIGRATION:
    migrate(db)

from routes.backend import *
from routes.frontend import *
from routes.api import *

@app.errorhandler(404)
def pageNotFound(error):
    return 'Page Not Found', 404

if __name__ == "__main__":
    app.run(debug = True, port = PORT, host = DATABASE_HOST)