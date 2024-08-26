# Импортируем в модуль функции divide из модулей fake_math и true_math,
#   назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён
# from fake_math import divide as fake_divide
# from true_math import divide as true_divide

# import true_math
# a = true_math.divide(12, 0)
# print(a)



# Ввриант_2
# Импортируем модули с переименовыванием на fm и tm
import fake_math as fm
import true_math as tm


# присваиваем значения для ф-ции divide из двух импортируемых модулей
fake_divide = fm.divide
true_divide = tm.divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# вывод результата
print(result1)
print(result2)
print(result3)
print(result4)

