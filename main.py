import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Временной интервал
t = np.linspace(0, 10, 500)

# Определение функций для сферических координат
r = 1 + 0.3 * np.sin(20 * t)
phi = t
theta = -np.exp(-0.001 * t) + np.pi / 2

# Преобразование сферических координат в декартовы
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Настройка графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Animated Trajectory')

# Создание точки для анимации
point, = ax.plot([], [], [], 'ro')  # 'ro' означает красная точка
trajectory_line, = ax.plot([], [], [], 'b-')  # 'b-' означает синяя линия


# Инициализация функции
def init():
    point.set_data([], [])
    point.set_3d_properties([])
    trajectory_line.set_data([], [])
    trajectory_line.set_3d_properties([])
    return point, trajectory_line


# Функция обновления для анимации
def update(frame):
    # Обновляем позицию точки
    point.set_data(x[frame:frame + 1], y[frame:frame + 1])  # Передаем массив длиной 1
    point.set_3d_properties(z[frame:frame + 1])  # Передаем массив длиной 1

    # Обновляем данные для линии
    trajectory_line.set_data(x[:frame + 1], y[:frame + 1])  # Все данные до текущего кадра
    trajectory_line.set_3d_properties(z[:frame + 1])  # Все данные до текущего кадра

    return point, trajectory_line


# Создание анимации
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

# Сохранение анимации в формате GIF
ani.save('trajectory_animation.gif', writer='pillow', fps=30)

plt.show()
