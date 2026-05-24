import random
n=input("Digite o nome de um(a) estudante ")
n2=input("Digite o nome outro(a) estudante ")
n3=input("Digite o nome de mais um(a) estudante ")
n4=input("Digite o nome do(a) último(a) estudante ")
lista=[n,n2,n3,n4]
random.shuffle(lista)
print(f"A lista de apresentação ficou: {lista}")