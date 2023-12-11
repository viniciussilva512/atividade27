# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_pares = 0
 
for i in range(6):
    numero = int(input(f"Digite o {i+1}° número: "))
    
    if numero % 2 == 0:
        soma_pares += numero
        
        
print(f"A soma dos números pares é: {soma_pares}")