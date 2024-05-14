import matplotlib.pyplot as plt
import cv2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Отображение гистограммы
axes[0].set_title(f'Комбинированная гистограмма')
axes[0].set_xlabel('Яркость')
axes[0].set_ylabel('Частота')
images_names_of_type_ = ['red.png', 'red.png', 'red.png', 'red.png', 'red.png']
images_of_type_ = [cv2.imread(f'./generated-or-not/chek_images/{img_name}') for img_name in images_names_of_type_]

# Построение общей гистограммы для каждого канала цвета (красный, зелёный, синий)
colors = ('r', 'g', 'b')
for i, col in enumerate(colors):
    col_vals = [image[:, :, i].flatten() for image in images_of_type_]
    hist = cv2.calcHist(col_vals, [0], None, [256], [0, 256])
    axes[1].plot(hist, color=col, label=col)
    axes[1].set_xlim([0, 256])

axes[0].set_title(f'Поканальная гистограмма изображений')
axes[1].set_xlabel('Яркость')
axes[1].set_ylabel('Частота')

plt.tight_layout()
plt.show()
