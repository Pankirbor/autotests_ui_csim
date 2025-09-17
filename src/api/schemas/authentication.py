from pydantic import BaseModel


class AuthenticationUserSchema(BaseModel):
    """Класс для валидации данных пользователя при аутентификации."""
