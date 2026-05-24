import math
n=float(input("Digite o valor de um ângulo"))
s= math.sin(math.radians(n))
cos= math.cos(math.radians(n))
tan= math.tan(math.radians(n))
print(f"Pelo valor de {n}\u00b0 do ângulo, o seno é: {s:.5f}, o Cosseno é: {cos:.5f} e o Tangente é: {tan:.5f}")
