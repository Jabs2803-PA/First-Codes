import random
n1=int(input("O computador vai pensar em um número de 0 a 5, tente acertar!"))
m=random.randint(1,5)
if n1==m:
    print(f"Você chutou {n1} e o número escolhido era...\n{m}! Você acertou!")
else:
    print(f"Você chutou {n1} e o número escolhido era...\n{m}... Não foi dessa vez.")
