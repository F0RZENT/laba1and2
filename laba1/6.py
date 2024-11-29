temperature = float(input("Введите температуру воды: "))
if temperature <= 0:
    print("Состояние воды: твердое")
elif temperature < 100:
    print("Состояние воды: жидкое")
else:
    print("Состояние воды: газообразное")