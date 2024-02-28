contatos = {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "emerson@gmail.com", {}
)  # {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}
print(resultado)
