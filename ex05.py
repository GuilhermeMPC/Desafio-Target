'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def inverter(frase):
    return frase[::-1]

string = "Target Sistemas, me contrata!"
string_invertida = inverter(string)

print("############")
print(string_invertida)
print("############")