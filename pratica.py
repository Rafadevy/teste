#programa para calcular media 

n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
n3 = int(input("digite outro numero: "))
resultado = (n1 + n2 + n3) / 3

print(f"Media do aluno: {resultado}")


if (resultado > 6):
     print("aluno aprovado. ")
elif (resultado <= 6):
     print("alunos reprovado. ")

#programa para calcular desconto

n1 = float(input("digite o valor do produto R$: "))
n2 = int(input("qual o valor do desconto: "))
desconto = (n1 * n2) / 100

print(f"o desconto é de: R${desconto}")

#Calculadora simples

def soma(n1, n2):
  return n1 + n2

def multiplicaçao(n1, n2):
  return n1 * n2

def subtraçao(n1, n2):
  return n1 - n2

def divisao(n1, n2):
  return n1 / n2

recept = (input("Qual operaçao voce quer fazer? (soma,subtraçao,divisao,multiplicaçao) ")).strip() .lower()

n1 = float(input("digite o numero: "))
n2 = float(input("digite o numero: "))

if recept == "soma":
  print(f"Resultado: {soma(n1, n2)}")

elif recept == "subtraçao":
  print(f"Resultado : {subtraçao(n1,n2)}")

elif recept == "multiplicacao":
  print(f"Resultado: {multiplicaçao(n1, n2)}")

elif recept == "divisao":
  print(f"Resultado: {divisao(n1, n2)}")
else:
  print("Operação inválida.")

#Numeros primos

num = int(input("Digite um número: "))
tot = 0

def é_primo_ou_nao(x):
    global tot
    for c in range(1, x + 1):
        if x % c == 0:
            print("\033[34m", end="")
            tot += 1
        else:
            print("\033[m", end="")
        print(f"{c}", end=" ")
    print() 

é_primo_ou_nao(num)

print(f"O número {num} foi divisível por {tot} números.")
if tot == 2:
    print("É primo!!")
else:
    print("Não é primo.")

#analise de dados 


from datetime import date
ano = date.today().year
tomaior = 0
tomenor = 0

for c in range (1,8):
    ans = int(input(f"em que ano a {c} pessoa nsceu? "))
    idade = ano - ans
    if idade >= 21:
        tomaior += 1
    else:
        tomenor += 1
print(f"ao todo tivemos {tomaior} pessoas maiores de idade")
print(f"e tambem tivemos {tomenor} pessoas de menor")

#Analise de dados 

somaidade = 0
maisvelhohomem = 0
nomevelho = ""
totmulher20 = 0

for p in range (1,5):
    print(f"------{p}ª PESSOA------" * 1)
    nome = str(input("Qaul seu nome:"))
    idade = int(input("digitte sua idade:"))
    sexo = str(input("Sexo [M/F]:")).upper()

    somaidade += idade

    if sexo == "M" and (p == 1 or idade > maisvelhohomem):
        maisvelhohomem = idade
        nomevelho = nome
    
    if sexo in "F" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f"a media e {mediaidade}")
print(f"o homem mais velho tem {maisvelhohomem} anos e se chama {nomevelho}")
print(f"ao todo sao {totmulher20} mulheres com menos de 20 anos")


toth = 0
totm20 = 0
while True:
    id = int(input("IDADE: "))
    sexo = (input("SEXO [M/F] ")).strip().upper()
    while sexo not in "MF":
        print("DIGITE UMA OPCAO VALIDA")
        sexo = input("SEXO [M/F]: ").strip().upper()

    if id >= 18:
        tot18 += 1
    if sexo == "H":
        toth += 1
    if sexo == "F" and id < 20:
        totm20 += 1

    resp = input("QUER CONTINUAR? ").strip().upper()
    while resp not in "SN":
        print("QUER CONTINUAR? [S/N]")
    if resp == "N":
       break

print(f"O numero de maiores de idade é {tot18}")
print(f"O numero de homem cadastrados é {toth}")
print(f"O numero de mulheres com menos de 20 anos é {totm20}")




