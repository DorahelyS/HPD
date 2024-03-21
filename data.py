import requests

url = 'http://localhost:5555/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)  
else:
    print('Failed to fetch data:', response.status_code)