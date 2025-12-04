from fastapi import FastAPI
from app.api.routes import products, users, login
from app.core.middleware import log_requests
from app.core.logging import logger

app = FastAPI(title="FastAPI Workshop Project")

# Middleware
app.middleware("http")(log_requests)

# Подключаем роутеры
app.include_router(products.router)
app.include_router(users.router)
app.include_router(login.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Приложение запущено")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Приложение остановлено")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)