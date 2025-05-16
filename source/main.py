from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.guest import router as guests_router
from routes.order import router as orders_router
from routes.room import router as rooms_router

app = FastAPI(title="Hotel Management API", description="API для управления отелем")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(guests_router)
app.include_router(orders_router)
app.include_router(rooms_router)
