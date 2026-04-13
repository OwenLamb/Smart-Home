import os
import requests
from dotenv import load_dotenv

load_dotenv()

HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")

headers = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

def get_state(entity):
    response = requests.get(
        f"{HA_URL}/api/states/{entity}",
        headers=headers,
        timeout=10
    )
    print(f"GET state response: {response.status_code}")
    print(response.text)

def turn_on_light(entity, brightness=None, rgb=None):
    data = {"entity_id": entity}

    if brightness is not None:
        data["brightness"] = int(brightness)

    if rgb is not None:
        data["rgb_color"] = rgb

    print("Sending:", data)

    response = requests.post(
        f"{HA_URL}/api/services/light/turn_on",
        headers=headers,
        json=data,
        timeout=10
    )

    print(f"Turn ON response: {response.status_code}")
    print(response.text)

def turn_off_light(entity):
    response = requests.post(
        f"{HA_URL}/api/services/light/turn_off",
        headers=headers,
        json={"entity_id": entity},
        timeout=10
    )

    print(f"Turn OFF response: {response.status_code}")
    print(response.text)

turn_on_light("light.lamp", 255, [255, 0, 0])
turn_on_light("light.lamp_2", 255, [0, 255, 0])
turn_on_light("light.lamp_3", 255, [0, 0, 255])