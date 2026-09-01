from datetime import datetime

def solution_station_2(date_str):
    japanese_days = {
        0: "月曜日",
        1: "火曜日",
        2: "水曜日",
        3: "木曜日",
        4: "金曜日",
        5: "土曜日",
        6: "日曜日",
    }
    
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date_obj.weekday()
    
    return japanese_days[weekday]
