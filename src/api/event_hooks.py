import allure
from httpx import Request, Response

from utils.http_curl import make_curl_request
from utils.logger import get_logger


logger = get_logger("HTTP_CLIENT")


def curl_event_hook(request: Request) -> None:
    """
    Записывает cURL команду в Allure.

    Args:
        request (Request): Запрос, который будет выполнен.
    """
    curl_command = make_curl_request(request=request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request) -> None:
    """
    Логирует запрос.

    Args:
        request (Request): Запрос, который будет выполнен.
    """
    logger.info(f"Отправляем запрос: {request.method} на {request.url}")


def log_response_event_hook(response: Response) -> None:
    """
    Логирует ответ.

    Args:
        response (Response): Ответ сервера.
    """
    logger.info(
        f"Получаем ответ: {response.status_code} {response.reason_phrase} от {response.url}"
    )
