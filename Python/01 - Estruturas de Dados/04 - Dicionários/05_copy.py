contatos = {"emerson@gmail.com": {"nome": "Emerson", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["emerson@gmail.com"] = {"nome": "Emerson"}

print(contatos["emerson@gmail.com"])  # {"nome": "Emerson", "telefone": "3333-2221"}

print(copia["emerson@gmail.com"])  # {"nome": "Emerson"}
