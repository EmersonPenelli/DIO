contatos = {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('emerson@gmail.com', {'nome': 'Emerson', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
