import json

d1 = {
    'Pessoa 1 ': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2 ': {
        'nome': 'Renato',
        'idade': 24,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
     file.write(d1_json)

