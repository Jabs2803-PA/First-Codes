n=float(input("Digite 3 valores em cm, e te direi se podem formam um triângulo! Primeiro valor:"))
n2=float(input("Segundo valor:"))
n3=float(input("Terceiro valor:"))
if n+n2<n3:
    print(f"Seu triângulo pode ser formado!")
elif n+n2>=n3:
    print(f"Seu triângulo não pode ser formado!")
elif n+n3<n2:
    print(f"Seu triângulo pode ser formado!")
elif n+n3>=n2:
    print(f"Seu triângulo não pode ser formado!")
elif n2+n3>n:
   print(f"Seu triângulo pode ser formado!")
elif n2+n3>=n:
    print(f"Seu triângulo não pode ser formado!")
