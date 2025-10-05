import random

def salvar_vetor(nome_arquivo, vetor):
    with open(nome_arquivo, "w") as f:
        f.write(" ".join(map(str, vetor)))


if __name__ == "__main__":

    # 1) Vetor para achar M
    Achar_M = [random.randint(0, 10000) for _ in range(1000)]
    salvar_vetor("vetor_Achar_M.txt", Achar_M)

    # 2) Vetor aleatório
    aleatorio = [random.randint(0, 10000) for _ in range(10000)]
    salvar_vetor("vetor_aleatorio.txt", aleatorio)

    # 3) Vetor ordenado em ordem crescente (pior caso)
    ordenado = random.sample(range(10000), 6000)
    ordenado.sort()
    salvar_vetor("vetor_ordenado.txt", ordenado)

    # 4) Vetor ordenado em ordem decrescente (pior caso)
    inverso = random.sample(range(10000), 7000)
    inverso.sort(reverse=True)
    salvar_vetor("vetor_inverso.txt", inverso)

    # 5) Vetor com muitos elementos repetidos (apenas 5 valores possíveis)
    repetidos = [random.choice([1, 2, 3, 4, 5]) for _ in range(8000)]
    salvar_vetor("vetor_repetidos.txt", repetidos)


    print("Massas de teste geradas com sucesso!")