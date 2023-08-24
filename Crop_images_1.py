import os
from PIL import Image

def crop_images(input_folder, output_folder, left, upper, right, lower):
    try:
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(input_folder):
            if filename.endswith(".png"):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                image = Image.open(input_path)
                cropped_image = image.crop((left, upper, right, lower))
                cropped_image.save(output_path)
                
                print(f"Обрезано изображение: {filename}")

        print("Обрезание изображений завершено.")

    except Exception as e:
        print("Произошла ошибка:", str(e))

input_folder = "D:\Request\Kapcha\other_png_full_2"
output_folder = "D:\Request\Kapcha\other_png_mini_2"

left = 275
upper = 157
right = 1072
lower = 600

crop_images(input_folder, output_folder, left, upper, right, lower)
