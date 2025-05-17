from pydantic import BaseModel
from typing import Optional

class Room(BaseModel):
    """
    Модель данных для таблицы rooms.
    Представляет информацию о комнатах отеля.
    """
    room_id: Optional[int] = None
    number: str
    capacity: int
    is_available: bool
    light_status: bool
    temperature: float
    humidity: float
    pressure: float
    door_status: bool
    price_per_night: float

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "number": "101",
                "capacity": 2,
                "is_available": True,
                "light_status": False,
                "temperature": 22.5,
                "humidity": 45.0,
                "pressure": 1013.0,
                "door_status": False,
                "price_per_night": 12.12
            }
        }

class RoomDataUpdate(BaseModel):
    """
    Модель для обновления показателей датчиков.
    """
    light_status: bool
    door_status: bool
    temperature: float
    humidity: float
    pressure: float
 
    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "light_status": True,
                "door_status": True,
                "temperature": 22.5,
                "humidity": 45.0,
                "pressure": 1013.0
            }
        }
