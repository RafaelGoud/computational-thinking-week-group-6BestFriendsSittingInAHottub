def solution_station_2=(date_str):
    chinese_days = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日",
    }
    
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date_obj.weekday()
    
    return chinese_day[weekday]
