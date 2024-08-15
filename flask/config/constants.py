import pathlib
basePath = str(pathlib.Path().resolve())

BASE_PATH = basePath
ADMIN_VIEW_FOLDER = "admin/"
DATABASE_NAME = "flask"
DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWORD = ""
DATABASE_DRIVER = "mysql"
RUN_MIGRATION = False
PORT = 5000