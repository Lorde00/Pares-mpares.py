pares = []
impares = []

for numeros in range(10): 
    numeros = float(input('Digite 10 números inteiros: '))
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
        
print(f'A soma dos números pares dados é igual a: {sum(pares)}')
print(f'A soma dos números ímpares é igual a: {sum(impares)}')
print(f'A soma dos números pares e ímpares é de: {sum(pares) + sum(impares)}')       
