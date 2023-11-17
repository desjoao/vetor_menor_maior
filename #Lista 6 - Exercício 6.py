real = [0]*15
maior = 0
menor = 0
posmen = 0
posmai = 0

for i in range(15):
    real[i] = float(input('Informe um número: '))
    if i == 0:
        maior = real[i]
        menor = real[i]
    elif real [i] < menor:
        menor = real[i]
        posmen = i
    elif real[i] > maior:
        maior = real[i]
        posmai = i

print(f'Os números informados foram {real}. \nO maior número informado é: {maior} e ele ocupa a {posmai + 1}ª posição no vetor. \nO menor número informado é: {menor} e ele ocupa a {posmen + 1}ª posição no vetor.')
