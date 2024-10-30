import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла методом Монте-Карло
def monte_carlo_integration(f, a, b, n=100000):
    x = np.random.uniform(a, b, n)
    y = f(x)
    integral = (b - a) * np.mean(y)
    return integral

# Обчислення методом Монте-Карло
integral_mc = monte_carlo_integration(f, a, b)
print(f"Інтеграл (Монте-Карло): {integral_mc}")

# Обчислення за допомогою функції quad
integral_quad, error = spi.quad(f, a, b)
print(f"Інтеграл (quad): {integral_quad}, помилка: {error}")

# Аналітичний розв'язок
integral_analytic = (b**3 - a**3) / 3
print(f"Інтеграл (аналітичний): {integral_analytic}")

# Порівняння результатів
print(f"Відхилення Монте-Карло від аналітичного: {abs(integral_mc - integral_analytic)}")
print(f"Відхилення quad від аналітичного: {abs(integral_quad - integral_analytic)}")