import sympy as sp

# Определяем переменную времени
t = sp.symbols('t')

# Определяем функции в сферических координатах
r_t = 1 + 0.3 * sp.sin(20 * t)
phi_t = t
theta_t = -sp.exp(-0.001 * t) + sp.pi / 2

# Преобразуем в декартовы координаты
x_t = r_t * sp.sin(theta_t) * sp.cos(phi_t)
y_t = r_t * sp.sin(theta_t) * sp.sin(phi_t)
z_t = r_t * sp.cos(theta_t)

# Находим скорость (производная положения по времени)
v_x = sp.diff(x_t, t)
v_y = sp.diff(y_t, t)
v_z = sp.diff(z_t, t)

# Вычисляем модуль скорости
speed = sp.sqrt(v_x**2 + v_y**2 + v_z**2)

# Пройденный путь как функция от времени (интеграл скорости)
path_function = sp.integrate(speed, t)

# Определяем t1 и t2
t1 = 1
t3 = 1.3

# Вычисляем пройденный путь между t1 и t2
path_t1_t3 = path_function.subs(t, t3) - path_function.subs(t, t1)

# Печатаем результаты
print("Пройденный путь как функция от времени:", path_function)
print("Пройденный путь между t1 и t3:", path_t1_t3)
