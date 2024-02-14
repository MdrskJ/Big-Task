from io import BytesIO
import os.path

import requests
from PIL import Image


def get_pict(lon: str, lat: str, spn: str):
    map_path = f"data/map_image_spn={spn}.jpg"
    if os.path.isfile(map_path):
        return map_path

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([spn, spn]),
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    map_image = Image.open(BytesIO(response.content))
    map_image = map_image.convert("RGB")
    map_image.save(map_path, 'JPEG')
    return map_path
