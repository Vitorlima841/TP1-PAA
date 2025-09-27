import random

# Gerar 10.000 números inteiros aleatórios entre 1 e 100
numeros = [str(random.randint(1, 100)) for _ in range(1000)]

# Salvar em um arquivo .txt, um número por linha
with open("numeros_aleatorios.txt", "w") as f:
    f.write("\n".join(numeros))
