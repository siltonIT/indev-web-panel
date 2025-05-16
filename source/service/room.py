import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from source import config
from source.models.room import (
    Room,
    RoomLightUpdate,
    RoomAvailableUpdate,
    RoomDoorUpdate,
    RoomDataUpdate
)
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
    def get_room_by_id(room: Room) -> Dict[str, Any]:
        """Получает комнату по ID."""
        if room.room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
        
        response = config.supabase.table("rooms").select("*").eq("room_id", room.room_id).execute()
        if not response.data:
            raise HTTPException(
                status_code=404, 
                detail=f"Комната с id={room.room_id} не найдена"
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
    def update_room_availability(room: RoomAvailableUpdate) -> Dict[str, Any]:
        """Обновляет статус доступности комнаты."""
        if room.room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = (
            config.supabase.table("rooms")
            .update({"is_available": room.is_available})
            .eq("room_id", room.room_id)
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]

    @staticmethod
    def update_room_light_status(room: RoomLightUpdate) -> Dict[str, Any]:
        """Обновляет статус освещения в комнате."""
        if room.room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = (
            config.supabase.table("rooms")
            .update({"light_status": room.light_status})
            .eq("room_id", room.room_id)
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]

    @staticmethod
    def update_room_door_status(room: RoomDoorUpdate) -> Dict[str, Any]:
        """Обновляет статус двери в комнате."""
        if room.room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = (
            config.supabase.table("rooms")
            .update({"door_status": room.door_status})
            .eq("room_id", room.room_id)
            .execute()
        )
        if not response.data:
            raise HTTPException(status_code=404, detail="Комната не найдена")
        return response.data[0]

    @staticmethod
    def update_room_sensor_data(room: RoomDataUpdate) -> Dict[str, Any]:
        """Обновляет данные датчиков в комнате."""
        if room.room_id is None:
            raise HTTPException(status_code=400, detail="ID комнаты не указан")
            
        response = (
            config.supabase.table("rooms")
            .update({
                "temperature": room.temperature,
                "humidity": room.humidity,
                "pressure": room.pressure
            })
            .eq("room_id", room.room_id)
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
