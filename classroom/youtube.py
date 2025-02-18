import requests

url = "https://api.ssyoutube.com/api/convert"
payload = {
    "url": "https://www.youtube.com/watch?v=MNkmdNCyBsw",
    "format": "mp4"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
