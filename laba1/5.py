angle1 = float(input("Введите первый угол (гралусы): "))
angle2 = float(input("Введите второй угол (градусы): "))
angle3 = 180 - (angle1 + angle2)

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("Треугольник существует.")
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Треугольник прямоугольный.")
    else:
        print("Треугольник не является прямоугольным.")
else:
    print("Треугольник не существует.")