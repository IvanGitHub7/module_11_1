#Взаимодействие с библиотекой requests:
import requests

url = 'https://github.com/IvanGitHub7/module_11_1'
response = requests.get(url)
print('Статус запроса: ', response.status_code)
if response.status_code == 200:
    print(response.text)
else:
    print(f'Ошибка {response.status_code}: Не удалось получить данные')

#Взаимодействие с библиотекой pillow:
from PIL import Image
import image
from PIL import ImageDraw
from PIL import ImageFont

image_path = './module_11_1/pillow.PNG'

#Поворот изображения наи 45 градусов:
image = Image.open(image_path)
angle = 45
rotated_image = image.rotate(angle)
rotated_image.show()
rotated_image.save('./module_11_1/rotated_image.jpg')
rotated_image.close()

#Изменение цвета изображения:
filtered_image = Image.open('./module_11_1/rotated_image.jpg')
data = filtered_image.getdata()
new_data = []
for item in data:
    if item == (0, 0, 0):
        new_data.append((255, 255, 255))
    else:
        new_data.append(item)
filtered_image.putdata(new_data)
filtered_image.save('./module_11_1/filtered_image.jpg')
filtered_image.show()
filtered_image.close()

#Добавление надписи на изображение:
title_image = Image.open('./module_11_1/pillow.PNG')
draw = ImageDraw.Draw(title_image)
font = ImageFont.truetype("arial.ttf", size=36)
text = "I use the pillow library"
position = (65, 130)
text_color = (0, 0, 0)
draw.text(position, text, fill=text_color, font=font)
title_image.save('./module_11_1/itle_image.jpg')
title_image.show()