import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from source.models.room import RoomDataUpdate

def parse_iot_data(raw_data: str) -> RoomDataUpdate:
    """
    Парсит строку данных от IoT-устройства в объект RoomDataUpdate.
    
    Args:
        raw_data (str): Строка данных, например:
            "Light: 1, Door: 1, Ch1: 1, Ch2: 1, Temp: 38.65°C, Pressure: 98157.80hPa, Humidity: 18.81%"

    Returns:
        IoTDeviceData: Объект с полями light, door, temp, pressure, humidity.

    Raises:
        ValueError: Если строка некорректна или данные не могут быть преобразованы.
    """
    try:
        data = {}
        for pair in raw_data.split(", "):
            key, value = pair.split(": ")
            if key in ["Ch1", "Ch2"]:
                continue
            if key in ["Light"]:
                data["light_status"] = bool(int(value))
            elif key in ["Door"]:
                data["door_status"] = bool(int(value))
            elif key == "Temp":
                data["temperature"] = float(value.replace("°C", ""))
            elif key == "Pressure":
                data["pressure"] = float(value.replace("hPa", ""))
            elif key == "Humidity":
                data["humidity"] = float(value.replace("%", ""))
        return RoomDataUpdate(**data)
    except (ValueError, KeyError) as e:
        raise ValueError(f"Ошибка при парсинге данных IoT: {str(e)}")

if __name__ == "__main__":
    test_data = "Light: 1, Door: 1, Ch1: 1, Ch2: 1, Temp: 38.65°C, Pressure: 98157.80hPa, Humidity: 18.81%"
    result = parse_iot_data(test_data)
    print(result)
