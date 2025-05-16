import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from source import config
from source.models.guest import Guest
from fastapi import HTTPException
from typing import List, Dict, Any

class GuestService:
    @staticmethod
    def insert_guest(guest: Guest) -> Dict[str, Any]:
        """Добавляет нового гостя в базу данных."""
        response = config.supabase.table("guests").insert(guest.dict(exclude={"guest_id"})).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="Не удалось добавить гостя")
        return response.data[0]

    @staticmethod
    def get_all_guests() -> List[Dict[str, Any]]:
        """Получает всеx гостей."""
        response = config.supabase.table("guests").select("*").execute()
        return response.data

    @staticmethod
    def delete_guest(guest_id: int | None) -> Dict[str, Any]:
        """Удаляет гостя."""
        if guest_id is None:
            raise HTTPException(status_code=400, detail="ID гостя не указан")
            
        response = config.supabase.table("guests").delete().eq("guest_id", guest_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Гость не найден")
        return response.data[0]
