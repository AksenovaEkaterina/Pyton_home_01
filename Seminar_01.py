# Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным.
day = int (input("Введите число от 1 до 7: "))
if (day not in range (1,8) ): print ("Неверное число")
if ( day in range (1,6)): print ("Будни")
elif (day in range (6,8)): print ("Выходной")
if (day == 1): print ("Понедельник")
if (day == 2): print ("Вторник")
if (day == 3): print ("Среда")
if (day == 4): print ("Четверг")
if (day == 5): print ("Пятница")
if (day == 6): print ("Суббота")
if (day == 7): print ("Воскресенье")