import requests

url = "https://notify-api.line.me/api/notify"

payload={}
files=[
  ('imageFile',('anya.jpg',open('/C:/Users/Administrator/Documents/GitHub/line/lineAPI/anya.jpg','rb'),'image/jpeg'))
]
headers = {
  'Authorization': 'Bearer hF4n9ndtL9yw2ip40tPF7iPulbrkypL4KFxs0DSsd9N'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

