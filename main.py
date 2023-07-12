
# https post requests and update

import requests
from datetime import datetime
USERNAME = "heritage"
TOKEN = "yueroehfjuhfuruvau"
GRAPH_ID = "pixel65"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding hours",
    "unit": "hr",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2023, month=7, day=11)
print(today)
# the strftime method formats the date received from the module into our desired display mode.

creation_data = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "13"
}
# response = requests.post(url=pixel_creation_endpoint, json=creation_data, headers=headers)
# print(response.text)

# working with "put" request for updated existing data

update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230712"

updated_data = {
    "quantity": "3"
}
# response = requests.put(url=update_pixel, json=updated_data, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)

