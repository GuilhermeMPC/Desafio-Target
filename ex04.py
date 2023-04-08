'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

def percentual(faturamento):
    faturamentos = []
    for estado in faturamento:
        faturamentos.append(estado["valor"])
    total = sum(faturamentos)
    percentuais = []
    for estado in faturamento:
        percentual = (estado["valor"] / total) * 100
        percentuais.append(round(percentual, 1))
    return percentuais


faturamento = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]

percentuais = percentual(faturamento)
count = 0

print("############")
for i in faturamento:
    if len(i["estado"]) == 2:
        print("O Estado de " + i["estado"] + " representou " + str(percentuais[count]) + "% do faturamento total")
    else:
        print("Os outros Estados representaram " + str(percentuais[count]) + "% do faturamento total")
    count += 1
print("############")
