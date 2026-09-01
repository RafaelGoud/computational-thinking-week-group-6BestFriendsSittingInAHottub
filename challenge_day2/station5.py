team_one = ["Ainas", "Tobit", "Yasmin", "Zoë", 
            "Iuliia", "Oumaima", "Klementyna", "Markus", "Mufang",
            "Ebony", "Yurui", "Nandini", "Nathan", "Tiara",
            "Ben", "Yuvraj", "Christopher", "Lula", "Muni"]

team_two = ["Huy Bao", "Sade", "Iris", "Katharina", "Minseo",
            "Alex", "Zeno", "Arwen", "Rajko", "Sylwia",
            "Christina", "Helen", "Vadim", "Mark", "Mats",
            "David", "Lora", "Quinn", "Tarling"]

team_three = ["Elizabeth", "Soelie", "Gabriel", "Jakub", "Luc",
              "Aleksandra", "Rongze", "Arnav", "Donna", "Milan",
              "Cris", "Yusef", "Jingqi", "Oliver", "Vaayu",
              "Afua", "Rafael", "Anna", "Daniel", "Nataly",]

team_four = ["Jeremy", "Yutong", "Krishiv", "Neel", "Yujie",
             "An", "Heer", "Paige", "Samir",
             "Amalia", "Rakin", "Douwe", "Illya", "Maria",
             "Lara", "Tom", "Lucas", "Michelle", "Oliwia"]

def solution_station_5(station5_input):
    if station5_input in team_one:
        return 1
    elif station5_input in team_two:
        return 2
    elif station5_input in team_three:
        return 3
    elif station5_input in team_four:
        return 4
    else:
        return None
