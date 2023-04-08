'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.'''

import json

def maior_valor(dados):
    maior = {"dia": 0, "valor": 0.0}
    for dado in dados:
        if dado["valor"] > maior["valor"]:
            maior["dia"] = dado['dia']
            maior["valor"] = dado["valor"]
    return maior    

def menor_valor(dados):
    menor = {}
    for dado in dados:
        try:
            if dado["valor"] == 0:
                continue

            if dado["valor"] < menor["valor"]:
                menor["dia"] = dado["dia"]
                menor["valor"] = dado["valor"]
        except:
            menor["dia"] = dado["dia"]
            menor["valor"] = dado["valor"]
    return menor

def media_valores(dados):
    valores = []
    for dado in dados:
        if dado["valor"] == 0:
                continue
        valores.append(dado["valor"])
    return sum(valores)/len(valores)

def dias_acima_da_media(media, dados):
    dias = 0
    for dado in dados:
        if dado["valor"] >= media:
            dias += 1
    return dias

arquivo = open('dados.json')
dados = json.load(arquivo)

maior = maior_valor(dados)
menor = menor_valor(dados)
media = media_valores(dados)
dias = dias_acima_da_media(media, dados)

print("############")
print("O menor valor de faturamento foi " + str(menor["valor"]) + " no dia " + str(menor["dia"]) + "\n")
print("O maior valor de faturamento foi " + str(maior["valor"]) + " no dia " + str(maior["dia"]) + "\n")
print(f"Nesse mês tivemos {str(dias)} dias que superaram a média mensal de {str(round(media, 2))}")
print("############")

arquivo.close()
