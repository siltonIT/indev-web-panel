from fastapi import APIRouter, HTTPException
from source.models.order import Order
from source.services.order import OrderService
from typing import List, Dict, Any

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Dict[str, Any])
async def add_order(order: Order):
    try:
        return OrderService.insert_order(order)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при добавлении заказа: {str(e)}")

@router.get("/", response_model=List[Dict[str, Any]])
async def list_orders():
    try:
        return OrderService.get_all_orders()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении заказов: {str(e)}")

@router.delete("/{order_id}", response_model=Dict[str, Any])
async def remove_order(order_id: int):
    try:
        return OrderService.delete_order(order_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении заказа: {str(e)}")
