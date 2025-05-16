import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, HTTPException
from source.models.guest import Guest
from source.services.guest import GuestService
from typing import List, Dict, Any

router = APIRouter(prefix="/guests", tags=["guests"])

@router.post("/", response_model=Dict[str, Any])
async def add_guest(guest: Guest):
    try:
        return GuestService.insert_guest(guest)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при добавлении гостя: {str(e)}")

@router.get("/", response_model=List[Dict[str, Any]])
async def list_guests():
    try:
        return GuestService.get_all_guests()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении гостей: {str(e)}")

@router.delete("/{guest_id}", response_model=Dict[str, Any])
async def remove_guest(guest_id: int):
    try:
        return GuestService.delete_guest(guest_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении гостя: {str(e)}")
