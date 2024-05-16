import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img = Image.open(os.path.join(folder_path, filename))
        images.append(img)
    return images


def calculate_color_distribution(images):
    colors = []
    for img in images:
        img_data = np.array(img)
        colors.extend(img_data.reshape(-1, img_data.shape[2]))

    return np.array(colors)


def plot_color_histogram(color_distribution):
    plt.figure(figsize=(10, 6))
    plt.hist(color_distribution, bins=256, color=['red', 'green', 'blue'], alpha=0.7)
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.title('Color Distribution')
    plt.show()


# Путь к вашему датасету с изображениями
dataset_folder = "./generated-or-not/chek_images/"

# Загрузка изображений
images = load_images(dataset_folder)

# Расчет распределения цветов
color_distribution = calculate_color_distribution(images)

# Построение гистограммы
plot_color_histogram(color_distribution)
