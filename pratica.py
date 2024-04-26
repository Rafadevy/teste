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

#Programa para calcular juros



