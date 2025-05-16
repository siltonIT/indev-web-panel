import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from source import config
from source.models.order import Order
from fastapi import HTTPException
from typing import List, Dict, Any

class OrderService:
    @staticmethod
    def insert_order(order: Order) -> Dict[str, Any]:
        """Добавляет нового заказ в базу данных."""
        response = config.supabase.table("orders").insert(order.dict(exclude={"order_id"})).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="Не удалось добавить гостя")
        return response.data[0]

    @staticmethod
    def get_all_orders() -> List[Dict[str, Any]]:
        """Получает всеx заказов."""
        response = config.supabase.table("orders").select("*").execute()
        return response.data

    @staticmethod
    def delete_order(order_id: int | None) -> Dict[str, Any]:
        """Удаляет заказ."""
        if order_id is None:
            raise HTTPException(status_code=400, detail="ID заказа не указан")
            
        response = config.supabase.table("orders").delete().eq("order_id", order_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Закакз не найден")
        return response.data[0]
