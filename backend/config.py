import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask app settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    DEBUG = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///heartburn_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Food database API settings
    FOOD_API_KEY = os.environ.get('FOOD_API_KEY') or 'your-food-api-key'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
