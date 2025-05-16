import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, HTTPException
from source.models.room import (
    Room,
    RoomLightUpdate,
    RoomAvailableUpdate,
    RoomDoorUpdate,
    RoomDataUpdate
)
from source.services.room import RoomService
from typing import List, Dict, Any

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.post("/", response_model=Dict[str, Any])
async def add_room(room: Room):
    try:
        return RoomService.insert_room(room)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при добавлении комнаты: {str(e)}")

@router.get("/", response_model=List[Dict[str, Any]])
async def list_all_rooms():
    try:
        return RoomService.get_all_rooms()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении комнат: {str(e)}")

@router.get("/available/", response_model=List[Dict[str, Any]])
async def list_available_rooms():
    try:
        return RoomService.get_available_rooms()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении доступных комнат: {str(e)}")

@router.get("/{room_id}", response_model=Dict[str, Any])
async def get_room(room_id: int):
    try:
        return RoomService.get_room_by_id(room_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении комнаты: {str(e)}")

@router.patch("/{room_id}/light/", response_model=Dict[str, Any])
async def update_room_light(room_id: int, light_update: RoomLightUpdate):
    try:
        light_update.room_id = room_id  # Добавляем room_id в модель
        return RoomService.update_room_light_status(light_update)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обновлении света: {str(e)}")

@router.patch("/{room_id}/availability/", response_model=Dict[str, Any])
async def update_room_availability(room_id: int, availability_update: RoomAvailableUpdate):
    try:
        availability_update.room_id = room_id  # Добавляем room_id в модель
        return RoomService.update_room_availability(availability_update)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обновлении доступности: {str(e)}")

@router.patch("/{room_id}/door/", response_model=Dict[str, Any])
async def update_room_door(room_id: int, door_update: RoomDoorUpdate):
    try:
        door_update.room_id = room_id  # Добавляем room_id в модель
        return RoomService.update_room_door_status(door_update)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обновлении статуса двери: {str(e)}")

@router.patch("/{room_id}/data/", response_model=Dict[str, Any])
async def update_room_data(room_id: int, data_update: RoomDataUpdate):
    try:
        data_update.room_id = room_id  # Добавляем room_id в модель
        return RoomService.update_room_sensor_data(data_update)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обновлении данных датчиков: {str(e)}")

@router.delete("/{room_id}", response_model=Dict[str, Any])
async def remove_room(room_id: int):
    try:
        return RoomService.delete_room(room_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении комнаты: {str(e)}")
