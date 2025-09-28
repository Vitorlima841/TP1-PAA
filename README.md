As versões implementadas foram:

QuickSort Recursivo (versão clássica).

QuickSort Híbrido → utiliza Insertion Sort para sub-vetores menores que um limite M. O valor ideal de M foi obtido empiricamente.

QuickSort Híbrido com Mediana-de-três → utiliza a técnica da mediana de três elementos para a escolha do pivô.

=======Massas de Teste=======

As massas de teste foram geradas no arquivo gerador_numeros.py. Foram considerados os seguintes casos:

vetor_aleatorio.txt → números em ordem aleatória.

vetor_ordenado.txt → números em ordem crescente.

vetor_inverso.txt → números em ordem decrescente (pior caso do QuickSort clássico).

vetor_repetidos.txt → vetor com muitos elementos repetidos.

Cada vetor possui 1000 elementos.

=======Estrutura do Repositório=======

Letra-A.py → Implementação do QuickSort recursivo.

Letra-B.py → QuickSort híbrido (com busca empírica do melhor M).

Letra-C.py → QuickSort híbrido com técnica da mediana-de-três.

gerador_numeros.py → gera as massas de teste (.txt).

Arquivos .txt → vetores de entrada para os experimentos.

=======Como Executar=======

Gere os vetores de teste:
python gerador_numeros.py

Alteração da variável arquivo:     

if __name__ == "__main__":

    arquivo = "nome_do_vetor_que_você_quer_testar.txt"

Execute cada versão do algoritmo:
python Letra-A.py
python Letra-B.py
python Letra-C.py

=======Metodologia de Testes=======

Cada execução é repetida 30 vezes para maior consistência.

Métricas coletadas:

Tempo médio de execução (em segundos).

Desvio padrão dos tempos (consistência dos resultados).

Número médio de comparações.

Número médio de trocas.

Os resultados são apresentados em tabelas e gráficos no relatório em LaTeX (Overleaf).

=======Resultados Esperados=======

O QuickSort híbrido deve superar o QuickSort puro em vetores aleatórios e repetidos, especialmente com valores adequados de M.

O QuickSort com mediana-de-três deve reduzir os impactos do pior caso (vetor ordenado e inverso).

A análise final busca o melhor valor de M e a eficiência relativa entre as versões.

=======Relatório=======

O relatório acadêmico foi produzido em LaTeX (Overleaf) e contém:

Introdução

Referencial teórico (QuickSort, Insertion Sort, análise de complexidade, pior caso)

Metodologia

Resultados e análise crítica

Conclusão

Referências bibliográficas

O link para o relatório em Overleaf será disponibilizado via Canvas.

=======Tecnologias Utilizadas=======

Python 3.13.7

Módulos padrão: time, statistics.






