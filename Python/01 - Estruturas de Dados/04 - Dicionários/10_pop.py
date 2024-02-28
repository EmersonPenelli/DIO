contatos = {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}}

resultado = contatos.pop("emerson@gmail.com")  # {'nome': 'Emerson', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("emerson@gmail.com", {})  # {}
print(resultado)
