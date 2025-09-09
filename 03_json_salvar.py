import json

# Lista de alunos (simulando dados que poderiam vir da nuvem)
alunos = [
    {"nome": "John", "curso": "ADS"},
    {"nome": "Robson", "curso": "CC"},
    {"nome": "Mary", "curso": "ADS"}
]

# Salvando em arquivo local
with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=4)
#json.dump grava a lista no formato json
#indent=4 formato para facilitar a leitura
print("Arquivo 'alunos.json' salvo com sucesso!")