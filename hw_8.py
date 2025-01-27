"""
hw_8.py: Модуль для сжатия изображений с помощью Pillow.
В данном дз нет коммитов в связи с тем, что оно было разобрано на уроке.
"""

from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
import pillow_avif 
import os


ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'webp', 'heic', 'avif']


# Регистрируем форматы
register_heif_opener()


def compress_image(file_path: str, quality: int = 50, format: str = 'avif') -> None:
    # поддерживаемые файлы
    supported_formats = ['webp', 'heic', 'avif']

    # проверка на поддерживаемый формат
    if format not in supported_formats:
        raise ValueError(f"Unsupported format: {format}")
    
    # открываем изображение
    image = Image.open(file_path)
    # сохраняем изображение в выбранном формате
    if format in ['webp', 'avif']:
        image.save(f"output.{format}", quality=quality)
        return
    if format == 'heic':
        heif_file = heif_from_pillow(image)
        heif_file.save(f"output.{format}", quality=quality)
        return


def get_images_path(source_path: str, allowed_extension: list[str]) -> list[str]:
    """
    рекурсивный обход директории или проверка одного файла для получения всех изображений
    - проверка: существует ли путь , валидность расширений(используйте ALLOWED_EXTENSIONS)
    """
    # проверка что путь существует 
    if not os.path.exists(source_path):
        raise ValueError(f"Path '{source_path}' does not exist.")


    # получаем, попка или файл:
    if os.path.isfile(source_path):
        return [source_path]
    

    images = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_ext = file.split('.')[-1].lower() # Приводим расширение к нижнему регистру
            if file_ext in allowed_extension:
                full_path = os.path.join(root, file)
                images.append(full_path)
    return images # Возвращаем список изображений


def main():
    user_path = input("Введите путь к изображению или директории: ").strip('"')
    images = get_images_path(user_path, ALLOWED_EXTENSIONS)

    for image in images:
        compress_image(image, format='avif')


if __name__ == '__main__':
    main()