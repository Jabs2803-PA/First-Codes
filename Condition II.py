n=float(input("Escolha um número para comparar com outros 2:"))
n2=float(input("Escolha outro!"))
n3=float(input("Escolha o último!"))
if n>n2 and n2>n3:
    print(f"O maior é {n} e o menor é {n3}!")
elif n2>n and n>n3:
    print(f"O maior é {n2} e o menor é {n3}!")
elif n3>n2 and n2>n:
    print(f"O maior é {n3} e o menor é {n}!")
elif n2>n and n3>n:
    print(f"O maior é {n2} e o menor é {n}!")
elif n3>n and n>n2:
    print(f"O maior é {n3} e o menor é {n2}!")
elif n>n3 and n3>n2:
    print(f"O maior é {n} e o menor é {n2}!")



