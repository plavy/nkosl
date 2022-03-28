import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "please_change-this_secret_key"
    # URI format: dialect+driver://username:password@host:port/database
    DB_USER = os.environ.get("DB_USER") or "nkosl"
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT") or "5432"
    DB_NAME = os.environ.get("DB_NAME") or "nkosl"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(DB_USER,
                                                                   DB_PASSWORD,
                                                                   DB_HOST,
                                                                   DB_PORT,
                                                                   DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
