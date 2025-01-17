# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

# print(response.status_code)
# print(response.headers)
# print(response.json())
print(response.text)


url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
print(response.json())

if response.status_code == 200:
    # Verifique o conteúdo da resposta
    print("Conteúdo retornado:", response.text)
    try:
        data = response.json()  # Tenta converter para JSON
        for item in data:
            print(item)
    except ValueError as e:
        print("Erro ao decodificar JSON:", e)
else:
    print(f"Erro na requisição: {response.status_code}")
