from loguru import logger

logger.add("logs/app.log", rotation="1 MB", retention="7 days", level="INFO")
logger.add(lambda msg: print(msg), level="DEBUG")  # вывод в консоль