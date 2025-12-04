from fastapi import Request
from app.core.logging import logger

async def log_requests(request: Request, call_next):
    logger.info(f"Запрос: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Статус ответа: {response.status_code}")
    return response