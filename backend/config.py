import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///notes.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret")
