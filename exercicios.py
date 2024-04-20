# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
print(numero_1 + numero_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_1 = int(input("Digite um número: "))
resto = numero_1 % 5
print(f"O resto da divisao do numero {numero_1} por 5 é  {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
print(numero_1 * numero_2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input('Inserir um numero inteiro:'))
numero_02 = int(input('Inserir um numero inteiro:'))
resultado = numero_01 // numero_02
print(resultado)
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_1 = int(input("Digite o primeiro numero: "))
quadrado = numero_1 ** 2
print(f"O quadrado do numero {numero_1} é {quadrado}")

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input('Digite um numero flutuante (float): '))
numero_2 = float(input('Digite um numero flutuante (float): '))
print(numero_1 + numero_2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input('Digite um numero flutuante (float): '))
numero_2 = float(input('Digite um numero flutuante (float): '))
media = (numero_1 + numero_2)/2 
print(f'a media desses dois numeros é {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input('Digite um numero flutuante (float): '))
expoente = int(input('Digite o expoente (float): '))
numero_final = base ** expoente
print(f'o numero final é {numero_final}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input('Digite a temperatura em celsius: '))
fahrenheit = (9/5) * celsius + 32
print(f'A temperatura em fahrenheit é : {fahrenheit}')
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math 
raio_do_circulo = float(input('Digite o raio: '))
area_do_circulo = round(math.pi * raio_do_circulo ** 2,2)
print(area_do_circulo)

##### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string_1 = input('Digite a primeira string: ')
upper = string_1.upper()
print(upper)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
string_1 = input('Digite o seu nome completo: ')
lower = string_1.lower()
print(lower)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
string_1 = input('Digite uma frase: ')
string_transformada = string_1.strip()
print(string_transformada)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('insira uma data no formato dd/mm/aaaa: ')
lista_data_separada = data.split('/')
print(f'Dia {lista_data_separada[0]} mes {lista_data_separada[1]} e ano {lista_data_separada[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_1 = input('Digite a primeira string: ')
string_2 = input('Digite a segunda string: ')
print(string_1+ string_2)

#### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool_1 = True 
bool_2 = False 
resultado = bool_1 and bool_2
print(f'Resultado logico de {bool_1} and {bool_2} é {resultado}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool_1 = True 
bool_2 = False 
resultado = bool_1 or bool_2
print(f'Resultado logico de {bool_1} or {bool_2} é {resultado}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool_1 = True 
bool_1_inverso = not bool_1
print(bool_1_inverso)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o primeiro numero: '))
resultado = (numero_1 == numero_2)
print(f'Os numeros fornecidos sao iguais? {resultado}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o primeiro numero: '))
resultado = (numero_1 == numero_2)
print(f'Os numeros fornecidos sao iguais? {resultado}')
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
