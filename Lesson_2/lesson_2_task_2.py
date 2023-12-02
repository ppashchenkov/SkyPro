def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: return False

year = int(input("Введите год: "))
no_visokosny = is_year_leap(year)

if no_visokosny: print("год",year,":","True")
else: print("год",year,":","False")