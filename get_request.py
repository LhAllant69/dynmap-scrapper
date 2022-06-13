from requests import get
import info

def get_info(address, world):
    data = get("http://{}/up/world/{}/0".format(address, world)).json()
    filtered_data = info.info(data)
    return filtered_data