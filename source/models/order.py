from datetime import date
from pydantic import BaseModel, validator
from typing import Optional

class Order(BaseModel):
    """
    Модель данных для таблицы orders.
    Представляет информацию о комнатах отеля.
    """
    order_id: Optional[int] = None
    room_id: int
    guest_id: int
    check_in_date: str 
    check_out_date: str

    @validator("check_out_date")
    def validate_dates(cls, v, values):
        if "check_in_date" in values and v < values["check_in_date"]:
            raise ValueError('Дата выезда должна быть позже даты заезда')
        return v

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "room_id": "1",
                "guest_id": "1",
                "check_in_date": "2025-05-21",
                "check_out_date": "2025-05-21"
            }
        }
