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
                "door_status": False
            }
        }


class RoomLightUpdate(BaseModel):
    """
    Модель для обновления статуса света в комнате.
    """
    room_id: Optional[int] = None
    light_status: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "light_status": True
            }
        }

class RoomAvailableUpdate(BaseModel):
    """
    Модель для обновления статуса занятости комнаты.
    """
    room_id: Optional[int] = None
    is_available: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "is_available": True
            }
        }
        
class RoomDoorUpdate(BaseModel):
    """
    Модель для обновления статуса двери.
    """
    room_id: Optional[int] = None
    door_status: bool

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "door_status": True
            }
        }

class RoomDataUpdate(BaseModel):
    """
    Модель для обновления показателей датчиков.
    """
    room_id: Optional[int] = None
    temperature: float
    humidity: float
    pressure: float
 
    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "temperature": 22.5,
                "humidity": 45.0,
                "pressure": 1013.0,
  
            }
        }
