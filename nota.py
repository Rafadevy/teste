n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
n3 = float(input("tericeira nota: "))

resultado = (n1 + n2 + n3) / 3

print(f"a media do aluno é {resultado}")

if (resultado >=6):
    print("aluno aprovado")
elif(resultado <6):
    print("aluno reprovado")

