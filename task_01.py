import pulp as pp

model = pp.LpProblem(name="Production_Optimization", sense = pp.LpMaximize)

# Визначення змінних
x1 = pp.LpVariable(name="Лимонад", lowBound=0)  # Кількість вироблених "Лимонадів"
x2 = pp.LpVariable(name="Фруктовий_сік", lowBound=0)  # Кількість вироблених "Фруктових соків"

# Цільова функція: максимізувати загальну кількість продуктів
model += x1 + x2, "Total_Production"

# Обмеження на ресурси
model += 2 * x1 + 1 * x2 <= 100, "Вода"
model += 1 * x1 <= 50, "Цукор"
model += 1 * x1 <= 30, "Лимонний_сік"
model += 2 * x2 <= 40, "Фруктове_пюре"

model.solve()

print(f"Статус: {model.status}, тобто {pp.LpStatus[model.status]}")
print(f"Максимальна кількість продуктів: {pp.value(model.objective)}")
print(f"Кількість вироблених 'Лимонадів': {pp.value(x1)}")
print(f"Кількість вироблених 'Фруктових соків': {pp.value(x2)}")