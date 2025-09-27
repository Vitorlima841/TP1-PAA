import random

def salvar_vetor(nome_arquivo, vetor):
    with open(nome_arquivo, "w") as f:
        f.write(" ".join(map(str, vetor)))


if __name__ == "__main__":
    n = 500  # tamanho do vetor

    # 1) Vetor aleatório
    aleatorio = [random.randint(0, 1000) for _ in range(n)]
    salvar_vetor("vetor_aleatorio.txt", aleatorio)

    # 2) Vetor já ordenado (crescente)
    ordenado = list(range(n))
    salvar_vetor("vetor_ordenado.txt", ordenado)

    # 3) Vetor ordenado de forma inversa (decrescente)
    inverso = list(range(n, 0, -1))
    salvar_vetor("vetor_inverso.txt", inverso)

    # 4) Vetor com muitos elementos repetidos (apenas 5 valores possíveis)
    repetidos = [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    salvar_vetor("vetor_repetidos.txt", repetidos)


    print("Massas de teste geradas com sucesso!")
