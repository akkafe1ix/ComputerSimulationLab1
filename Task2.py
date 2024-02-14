# Полностью автоматическое создание трендов с matplotlib
import matplotlib.pyplot as plt # импортируем построитель графиков из библиотеки matplotlib
import numpy as np # импортируем библиотеку numpy для работы с массивами numpy
from sklearn.metrics import r2_score # функция для расчёта критерия r^2

# график с точками
y = [917.8, 931, 921.4, 918.55, 929, 945.55, 953, 945.2, 907.6, 911.25, 941.9, 955.5, 961.8, 963.2, 979.4, 977.7, 978.6, 936.3, 940.6, 949.3, 962.2, 966.65, 1004.9, 997.30, 961.1]
x = [1,2,3,5,6,7,8,9,10,12,13,14,16,17,18,20,21,22,23,24,25,27,28,29,30]

# Массивы numpy по входным данным
numpy_x = np.array(x)
numpy_y = np.array(y)

# Линии тренда
# линейный (автоматическое создание)
set_line_by_data = np.polyfit(numpy_x, numpy_y, 1) # полином первой степени
linear_trend = np.poly1d(set_line_by_data) # снижение размерности до одномерного массива
print("{0}x + {1}".format(*set_line_by_data)) # формула

# полиномиальный
# set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6) # работа с полиномом 6 степени
# polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x
# print("${0}x^6 + {1}x^5 + {2}x^4 + {3}x^3 + {4}x^2 + {5}x + {6}$".format(*set_polinom_by_data)) # формула
# set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6)

set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 2) # работа с полиномом 2 степени
polinom_trend = np.poly1d(set_polinom_by_data) # Рассчитать значение полинома в точках x

polinom_title = "${0}x^2 + {1}x + {2}$".format(*set_polinom_by_data)
print("${0}x^2 + {1}x + {2}$".format(*set_polinom_by_data)) # формула

# логарифмический
set_log_by_data = np.polyfit(np.log(numpy_x), numpy_y, 1) # работа с полиномом 1 степени + логарифмирование x
log_trend = [set_log_by_data[0]*np.log(x) + set_log_by_data[1] for x in numpy_x] # создание одномерного массива для логарифмического тренда
print("${0}ln(x) + {1}$".format(*set_log_by_data))  # формула

# экспоненциальный
set_exp_by_data = np.polyfit(numpy_x, np.log(numpy_y), 1) # работа с полиномом 1 степени + логарифмирование
exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in numpy_x] # создание одномерного массива для экспоненциального тренда
print("${1}e^{0}x$".format(*set_exp_by_data))  # формула

# Расчёт R^2
linear_r2 = r2_score(numpy_y, linear_trend(numpy_x))
polinom_r2 = r2_score(numpy_y, polinom_trend(numpy_x))
log_r2 = r2_score(numpy_y, log_trend)
exp_r2 = r2_score(numpy_y, exp_trend)


# Отображение графиков
plt.figure(figsize=(15, 15)) # размер графика


# 2 графика по горизонтали, 2 по вертикали
plt.subplot(2, 2, 1)

# !!! Текущая ячейка - 1 (левый верхний график)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, linear_trend(numpy_x), linestyle='dashed', color="orange", label = 'linear trend') # линейный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='upper right', fontsize=12)
plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data))

# !!! Текущая ячейка - 2
plt.subplot(2, 2, 2)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
x = np.linspace(numpy_x.min(), numpy_x.max()) # набор данных для x для большей гладкости графика (50 точек)
plt.plot(x, polinom_trend(x), linestyle='dashed', color="orange", label = 'polinomial trend') # полиномиальный тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Полиномиальный \n$R^2=$" + str(polinom_r2) + polinom_title)

# !!! Текущая ячейка - 3
plt.subplot(2, 2, 3)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, log_trend, linestyle='dashed', color="orange", label = 'log trend') # логарифмический тренд
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'upper right', fontsize=12)
plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n${0}ln(x) + {1}$".format(*set_log_by_data))

# !!! Текущая ячейка - 4
plt.subplot(2, 2, 4)
plt.scatter(numpy_x, numpy_y, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot(numpy_x, exp_trend, linestyle='dashed', color="orange", label = 'exp trend')
plt.grid(color="gainsboro") # Сетка
plt.legend(loc = 'center left', fontsize=12, bbox_to_anchor=(1, 0.5))
plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n{1}e^({0}x)".format(*set_exp_by_data))

fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(15, 15) # Задать размеры графика

# Покажем окно с нарисованным графиком
plt.show()