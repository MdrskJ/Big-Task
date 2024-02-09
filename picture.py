from io import BytesIO

import requests

from PIL import Image
from PIL.ImageQt import ImageQt


def k():
    with open("const", encoding="utf-8") as f:
        data = f.readlines()
        lon, lat, delta = data[1].split()

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    # BytesIO(response.content)
    image = Image.open('pict1.jpg')
    image = image.convert("RGBA")
    ans = ImageQt(image)

    return ans
