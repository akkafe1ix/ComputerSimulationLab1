import pulp
from pulp import LpProblem, LpMinimize, value
import time


start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0, cat='Integer')
# Создаем задачу линейного программирования для минимизации
problem = LpProblem("Minimize",LpMinimize)
# Определяем целевую функцию для минимизации
problem += x1*5 + x2*6 + x3*7 + x4*4

# Определяем ограничения
problem += x1 + x2 + 4 * x4 >= 26
problem += 2*x1 + 3*x3 + 5*x4 >= 30 
problem += x1 + 2*x2 + 4*x3 + 6*x4 >= 24
#problem += x4>=9

# Решаем задачу
problem.solve()

# Выводим результаты
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("Стоимость:")
print(value(problem.objective))
stop = time.time()
print ("Время:")
print(stop - start)
