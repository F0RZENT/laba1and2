def get_season(month):
    if (1 <= month <= 12):
        return "Ошибка ввода: номер месяца должен быть в диапазоне от 1 до 12."
    
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"

month = int(input("Введите номер месяца: "))
print(get_season(month))
