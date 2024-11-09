import numpy as np
import matplotlib.pyplot as plt

# Создаем параметры
theta = np.linspace(0, 2 * np.pi, 100)

# Уравнения для рисования яиц с большим промежутком
x_egg_right = 0.5 * np.cos(theta) + 1  # Правая полусфера
y_egg_right = 0.5 * np.sin(theta) - 1  # Смещаем вниз

x_egg_left = 0.5 * np.cos(theta)  # Увеличиваем расстояние между яйцами
y_egg_left = 0.5 * np.sin(theta) - 1  # Смещаем вниз

x = 0.5 * np.cos(theta) + 0.5  # Увеличиваем расстояние между яйцами
y = 2 * np.sin(theta) + 0.9  # Смещаем вниз

# Уравнения для рисования ствола
stem_width = 0.5  # Ширина ствола
x_stem = np.full(100, stem_width)  # Центрируем ствол
y_stem = np.linspace(2, 2.9, 100)

stem_width = 0.5  # Ширина ствола
x1_stem = np.full(100, stem_width)  # Центрируем ствол
y1_stem = np.linspace(2, 2.9, 100)



# Создание графика
plt.figure(figsize=(6, 8))

# Рисуем яйца
plt.plot(x_egg_right, y_egg_right, color='r')
plt.plot(x_egg_left, y_egg_left, color='r')

plt.plot(x1_stem, y1_stem, color='r')

plt.plot(x, y, color='r')

# Рисуем ствол
plt.plot(x_stem, y_stem, color='r')

# Настройки графика
plt.xlim(-1.5, 1.5)
plt.ylim(-2, 3)
plt.axis('equal')
plt.axis('off')  # Отключить оси
plt.title('Форма мужского полового органа с увеличенным промежутком между яицами')
plt.savefig('писька.png')