from app.external.utils.config import ConfigUtils


SECRET_KEY = ConfigUtils.env('SECRET_KEY', str)
ENCRYPT_ALGORITHM = ConfigUtils.env('ENCRYPT_ALGORITHM', str)
