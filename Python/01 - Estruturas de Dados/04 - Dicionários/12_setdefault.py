contato = {"nome": "Emerson", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Emerson"
print(contato)  # {'nome': 'Emerson', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Emerson', 'telefone': '3333-2221', 'idade': 28}
