from passlib.context import CryptContext


class CryptDriver:
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")