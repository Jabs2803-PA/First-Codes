import random
n=input("Digite o nome de um(a) aluno(a)")
n2=input("Digite o nome de outro aluno(a)")
n3=input("Digite o nome mais um(a) aluno(a)")
n4=input("Digite o nome do(a) último(a) aluno(a)")
lista=[n,n2,n3,n4]
print(f"O aluno escolhido foi:{random.choice(lista)}")
