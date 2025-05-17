import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, HTTPException
from source.models.room import Room, RoomDataUpdate
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

@router.patch("/{room_id}/available/", response_model=Dict[str, Any])
async def update_room_availability(room_id: int, is_available: bool):
    try:
        return RoomService.update_room_availability(room_id, is_available)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обновлении доступности: {str(e)}")

@router.patch("/{room_number}/data/", response_model=Dict[str, Any])
async def update_room_data(room_number: str, data: RoomDataUpdate):
    try:
        return RoomService.update_room_sensor_data(room_number, data)
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
