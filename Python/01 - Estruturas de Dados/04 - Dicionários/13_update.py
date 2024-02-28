contatos = {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}}

contatos.update({"emerson@gmail.com": {"nome": "EMS"}})
print(contatos)  # {'emerson@gmail.com': {'nome': 'EMS'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'emerson@gmail.com': {'nome': 'Ems'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
