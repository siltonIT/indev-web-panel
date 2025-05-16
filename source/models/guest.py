from pydantic import BaseModel
from typing import Optional

class Guest(BaseModel):
    """
    Модель данных для таблицы guest.
    Представляет информацию о комнатах отеля.
    """
    guest_id: Optional[int] = None
    name: str
    email: str
    phone: str
    password_hash: str

    class Config:
        """
        Конфигурация Pydantic для модели.
        """
        json_schema_extra = {
            "example": {
                "name": "Sergei Lazaruk",
                "email": "sergei@gmail.com",
                "phone": "+375256109862",
                "password_hash": "dsjklfadjkdanbeb2i29fszdz7e4"
            }
        }


