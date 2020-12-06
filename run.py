import os

from config import app_config
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(app_config[config_name])


if __name__ == '__main__':
    app.run()
