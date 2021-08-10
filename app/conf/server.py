from app.external.utils.config import ConfigUtils

DEBUG = ConfigUtils.env('DEBUG', bool)
TITLE_API = ConfigUtils.env('TITLE_API', str)
DESCRIPTION_API = ''
VERSION_API = ConfigUtils.env('VERSION_API', str)

EXPIRE_ACCESS_TOKEN_MINUTES = EXPIRE_SECRET_CODE_MINUTES = 60 * 60 * 5  # 5 hours
SECRET_CODE_LEN = 8
EXPIRE_REFRESH_TOKEN_MINUTES = 3000
TOTAL_FILES_COUNT = 50
