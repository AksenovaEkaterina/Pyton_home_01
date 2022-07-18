# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
from operator import truediv
from sys import float_repr_style


Result = true
for X in true, folse:
    for Y in true, folse:
        for Z in true, folse:
            print (rezult (not (X or Y or Z)==(not X and not Y and not Z)))
