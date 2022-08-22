"""
data 관련 함수들
"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os


def load(root, type_index):
    ttv = ["train", "validation", "test"]

    path = join(root, ttv[type_index])
    return data_generator(path)

def join(root, path):
    return os.path.join(root, path)

def data_generator(path, target_size=(128,128), batch_size=20, class_mode="categorical"):
    datagen = ImageDataGenerator(1./255)
    return datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        class_mode=class_mode
    )

if __name__ == "__main__":
    load()