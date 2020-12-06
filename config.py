class Config(object):
    """
    """


class DevelopmentConfig(Config):
    """
    """
    DEBUG = True
    SQLALCHEMY = True


class ProductionConfig(Config):
    """
    """
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
