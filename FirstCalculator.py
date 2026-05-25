import math
print('Calculadora')
n3 = input("Digite a operação desejada:\nSoma(+)\nSubtração(-)\nMultiplicação(x)\nDivisão(/)\nExponenciação(^)\nRaiz Quadrada(/2)\nRaíz cúbica (/3)\nMais opções(M):\n")
if n3 == "M":
    n3 = input("Mais opções:\nSeno(S)\nCosseno(C)\nTangente(T)\nPi (P)\nLog (L)\nFatorial (F)\nValor absoluto (VA)\nArredondamento (Round)\nTeto (Ceil)\nPiso (Floor)\nLogaritimo Natural (Log)\nMáximo entre 2 Números (MX2)\nMínimo entre 2 Números (MI2)\nHipotenusa (H)\nGraus para radianos (GPR)\nRadiano para Graus (RPG)"
               ":\n")
    if n3 == "S":
        n = int(input("Digite um numero:"))
        print(math.sin(math.radians(n)))
    elif n3 == "C":
        n = int(input("Digite um numero:"))
        print(math.cos(math.radians(n)))
    elif n3 == "T":
        n = int(input("Digite um numero:"))
        print(math.tan(math.radians(n)))
    elif n3 == "P":
        print(math.pi)
    elif n3 == "L":
        n = float(input("Digite um numero:"))
        print(math.log10(n))
    elif n3 == "F":
        n = int(input("Digite um numero:"))
        print(math.factorial(n))
    elif n3 == "VA":
        n = int(input("Digite um numero:"))
        print(abs(n))
    elif n3== "Round":
        n = int(input("Digite um numero:"))
        print(round(n))
    elif n3 == "Ceil":
        n = int(input("Digite um numero:"))
        print(math.ceil(n))
    elif n3 == "Floor":
        n = int(input("Digite um numero:"))
        print(math.floor(n))
    elif n3 == "Log":
        n = int(input("Digite um numero:"))
        print(math.log(n))
    elif n3 == "MX2":
        n = int(input("Digite um numero:"))
        n2 = int(input("Digite outro numero:"))
        print(max(n, n2))
    elif n3 == "MI2":
        n = int(input("Digite um numero:"))
        n2 = int(input("Digite outro numero:"))
        print(min(n, n2))
    elif n3 == "H":
        n = int(input("Digite um numero:"))
        n2 = int(input("Digite outro numero:"))
        print(math.hypot(n, n2))
    elif n3 == "GPR":
        n = float(input("Digite um numero:"))
        print(math.radians(n))
    elif n3 == "RPG":
        n = float(input("Digite um numero:"))
        print(math.degrees(n))
elif n3 == "+":
    n = int(input("Digite um numero:"))
    n2 = float(input("Digite outro número:"))
    print(n + n2)
elif n3 == "-":
    n = int(input("Digite um numero:"))
    n2 = float(input("Digite outro número:"))
    print(n - n2)
elif n3 == "x":
    n = int(input("Digite um numero:"))
    n2 = float(input("Digite outro número:"))
    print(n * n2)
elif n3 == "/":
    n = int(input("Digite um numero:"))
    n2 = float(input("Digite outro número:"))
    print(n / n2)
elif n3 == "^":
    n = int(input("Digite um numero:"))
    n2 = float(input("Digite outro número:"))
    print(n ** n2)
elif n3 == "/2":
    n = int(input("Digite um numero:"))
    print(math.sqrt(n))
elif n3 == "/3":
    n = float(input("Digite um numero:"))
    print(n**  (1/3))

