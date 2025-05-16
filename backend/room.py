from pydantic import BaseModel
from typing import Optional

class Room(BaseModel):
    """
    Модель данных для таблицы rooms.
    Представляет информацию о комнатах отеля.
    """
    id: Optional[int] = None
    number: str
    capacity: int
    is_available: bool
    light_status: bool
    temperature: float
    humidity: float
    pressure: float
    door_status: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        schema_extra = {
            "example": {
                "number": "101",
                "capacity": 2,
                "is_available": True,
                "light_status": False,
                "temperature": 22.5,
                "humidity": 45.0,
                "pressure": 1013.0,
                "door_status": False
            }
        }


class RoomLightUpdate(BaseModel):
    """
    Модель для обновления статуса света в комнате.
    """
    light_status: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        schema_extra = {
            "example": {
                "light_status": True
            }
        }

class RoomAvailableUpdate(BaseModel):
    """
    Модель для обновления статуса занятости комнаты.
    """
    is_available: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        schema_extra = {
            "example": {
                "is_available": True
            }
        }
        
class RoomDoorUpdate(BaseModel):
    """
    Модель для обновления статуса двери.
    """
    door_status: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        schema_extra = {
            "example": {
                "door_status": True
            }
        }

class RoomDataUpdate(BaseModel):
    """
    Модель для обновления показателей датчиков.
    """
    temperature: float
    humidity: float
    pressure: float
 
    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        schema_extra = {
            "example": {
                "temperature": 22.5,
                "humidity": 45.0,
                "pressure": 1013.0,
  
            }
        }
