from app.external.utils.config import ConfigUtils


DB_PORT = ConfigUtils.env('DB_PORT', str)
DB_HOST = ConfigUtils.env('DB_HOST', str)
DB_PASSWORD = ConfigUtils.env('DB_PASSWORD', str)
DB_PRIMARY_NAME = ConfigUtils.env('DB_PRIMARY_NAME', str)
DB_LOGS_NAME = ConfigUtils.env('DB_LOGS_NAME', str)
DB_USER = ConfigUtils.env('DB_USER', str)

REDIS_HOST = ConfigUtils.env('REDIS_HOST', str)
REDIS_PORT = ConfigUtils.env('REDIS_PORT', int)
REDIS_PASSWORD = ConfigUtils.env('REDIS_PASSWORD', str)
