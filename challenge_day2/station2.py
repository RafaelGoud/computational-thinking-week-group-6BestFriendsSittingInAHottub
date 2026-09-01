def solution_station_2=(date_str):
    chinese_days = {
        0: "星期一",  # Monday
        1: "星期二",  # Tuesday
        2: "星期三",  # Wednesday
        3: "星期四",  # Thursday
        4: "星期五",  # Friday
        5: "星期六",  # Saturday
        6: "星期日",  # Sunday
    }
    
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date_obj.weekday()
    
    return chinese_day[weekday]
