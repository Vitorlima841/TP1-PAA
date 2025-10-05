As versões implementadas foram:

QuickSort Recursivo (versão clássica).

QuickSort Híbrido → utiliza Insertion Sort para sub-vetores menores que um limite M. O valor ideal de M foi obtido empiricamente.

QuickSort Híbrido com Mediana-de-três → utiliza a técnica da mediana de três elementos para a escolha do pivô.

=======Massas de Teste=======

As massas de teste foram geradas no arquivo gerador_numeros.py. Foram considerados os seguintes casos:

vetor_Achar_M.txt → utilizado para achar o melhor valor de M (1000 elementos)

vetor_aleatorio.txt → números em ordem aleatória (10000 elementos)

vetor_ordenado.txt → números em ordem crescente, pior caso do QuickSort (6000 elementos)

vetor_inverso.txt → números em ordem decrescente, pior caso do QuickSort (7000 elementos)

vetor_repetidos.txt → vetor com muitos elementos repetidos (8000 elementos)



=======Estrutura do Repositório=======

Letra-A.py → Implementação do QuickSort recursivo.

Letra-B.py → QuickSort híbrido (com busca empírica do melhor M).

Letra-C.py → QuickSort híbrido com técnica da mediana-de-três.

gerador_numeros.py → gera as massas de teste (.txt).

Arquivos .txt → vetores de entrada para os experimentos.

=======Como Executar=======

Gere os vetores de teste:
python gerador_numeros.py

Execute cada versão do algoritmo:
python Letra-A.py
python Letra-B.py
python Letra-C.py

=======Metodologia de Testes=======

O desenvolvimento do trabalho seguiu as seguintes etapas:
    • Implementação do Quicksort recursivo tradicional;
    • Implementação da versão híbrida, interrompendo a recursão para subvetores com menos de M elementos e utilizando Insertion Sort;
    • Implementação da versão híbrida com pivô definido pela técnica damediana-de-três;• Definição empírica do valor de M por meio de experimentos com             vetores de 1000 elementos;
    • Execução de testes em diferentes massas de dados:
        – Vetores aleatórios (10000 elementos);
        – Vetores já ordenados (6000 elementos);
        – Vetores ordenados de forma inversa (7000 elementos);
        – Vetores com muitos elementos repetidos (8000 elementos);
    OBS: Vetores ordenados e inversamente ordenados = pior caso.
    • O Insertion Sort foi executado 100 vezes, com o M variando de 1 a 100.
    • Foram coletadas métricas de tempo de execução, número de comparações e trocas de cada M ;
    • Enfim, o melhor M (com o tempo de execução menor) é escolhido.
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







