def solution_station_1(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    return b
