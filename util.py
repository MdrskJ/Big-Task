from io import BytesIO
import os.path

import requests
from PIL import Image


def get_pict(lon: str, lat: str, z: str):
    params = {
        "ll": ",".join([lon, lat]),
        "z": z,
        "l": "map",
    }
    map_path = "data/map_image_" + "_".join([f"{i}={params[i]}" for i in params])
    if os.path.isfile(map_path):
        return map_path

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    map_image = Image.open(BytesIO(response.content))
    map_image = map_image.convert("RGB")
    map_image.save(map_path, 'JPEG')
    return map_path
