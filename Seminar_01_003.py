#Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти
Coordinates = int (input("Введите номер четверти: "))
if (Coordinates == 1 ): print ("X > 0 and Y > 0")
elif (Coordinates == 2 ): print ("X < 0 and Y >0")
elif (Coordinates == 3 ): print ("X < 0 and Y <0")
elif (Coordinates == 4 ): print ("X > 0 and Y <0")