def month_to_season(month):
    if month in range(3,6): return "Весна"
    elif month in range(6,9): return "Лето"
    elif month in range(9,12): return "Осень"
    elif (month in range(1,3)) or (month == 12): return "Зима"
    else: return "Такого месяца нет"
