import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from source import config
from source.models.room import Room
from source.utilits.iot_data_parser import parse_iot_data
from fastapi import HTTPException
from typing import List, Dict, Any

class RoomService:
    @staticmethod
    def insert_room(room: Room) -> Dict[str, Any]:
        """Добавляет новую комнату в базу данных."""
        response = config.supabase.table("rooms").insert(room.dict(exclude={"room_id"})).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="Не удалось добавить комнату")
        return response.data[0]

    @staticmethod
    def get_room_by_id(room_id: int | None) -> Dict[str, Any]:
        """Получает комнату по ID."""
        if room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
        
        response = config.supabase.table("rooms").select("*").eq("room_id", room_id).execute()
        if not response.data:
            raise HTTPException(
                status_code=404, 
                detail=f"Комната с id={room_id} не найдена"
            )
        return response.data[0]

    @staticmethod
    def get_all_rooms() -> List[Dict[str, Any]]:
        """Получает все комнаты."""
        response = config.supabase.table("rooms").select("*").execute()
        return response.data

    @staticmethod
    def get_available_rooms() -> List[Dict[str, Any]]:
        """Получает все доступные комнаты."""
        response = config.supabase.table("rooms").select("*").eq("is_available", True).execute()
        return response.data

    @staticmethod
    def update_room_availability(room_id: int | None, is_available: bool) -> Dict[str, Any]:
        """Обновляет статус доступности комнаты."""
        if room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = (
            config.supabase.table("rooms")
            .update({"is_available": is_available})
            .eq("room_id", room_id)
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]

    @staticmethod
    def update_room_sensor_data(room_number: str | None, room_row: str) -> Dict[str, Any]:
        """Обновляет данные датчиков в комнате."""
        if room_number is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
           
        room = parse_iot_data(room_row)

        response = (
            config.supabase.table("rooms")
            .update({
                "light_status": room.light_status,
                "door_status": room.door_status,
                "temperature": room.temperature,
                "humidity": room.humidity,
                "pressure": room.pressure
            })
            .eq("number", room_number)
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]

    @staticmethod
    def delete_room(room_id: int | None) -> Dict[str, Any]:
        """Удаляет комнату."""
        if room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = config.supabase.table("rooms").delete().eq("room_id", room_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]
