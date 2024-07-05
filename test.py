import requests

url = f'https://pokeapi.co/api/v2/pokemon/1'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print (data['sprites']["other"]["home"]['front_default'])
else:
    print("Pikachu")