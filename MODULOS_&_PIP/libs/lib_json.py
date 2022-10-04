import json

cadastros = [
    {
        "Nome": "João",
        "Idade": 31,
        "Profissoes": ["Estagiário", "Dev Python", "Engenheiro de software"]
    },
    {
        "Nome": "Maria",
        "Idade": 35,
        "Profissões": ["Estagiária de Design", "Desenvolvedora Frontend"]
    }

]

print(json.dumps(cadastros, ensure_ascii=False, indent=True))  #Os dumps criam uma string
#O ensure_ascii é para nao quebrar a string para tranforma os acentos, então ele fica False para permanecer do jeito que está na string