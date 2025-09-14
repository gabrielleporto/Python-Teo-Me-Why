import math 
math.#qualquer função
________________________

import random
random.randint(1, 10)

________________________

x=["João", "Maria", "lucas"]
v = random.choice(x)

print(v)

________________________

import requests
url = "http://viacep.com.br/ws/190060100/json"
resposta = request.get(url)
dados = resposta.json()
dados 