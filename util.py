from io import BytesIO

import requests
from PIL import Image


def get_pict(lon: str, lat: str, spn_lon: str, spn_lat: str):
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([spn_lon, spn_lat]),
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    map_image = Image.open(BytesIO(response.content))
    map_image = map_image.convert("RGB")
    map_path = "data/map_image.jpg"
    map_image.save(map_path, 'JPEG')

    return map_path
