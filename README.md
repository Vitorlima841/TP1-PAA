As versões implementadas foram:

QuickSort Recursivo (versão clássica).

QuickSort Híbrido → utiliza Insertion Sort para sub-vetores menores que um limite M. O valor ideal de M foi obtido empiricamente.

QuickSort Híbrido com Mediana-de-três → utiliza a técnica da mediana de três elementos para a escolha do pivô.

===Massas de Teste===

As massas de teste foram geradas no arquivo gerador_numeros.py. Foram considerados os seguintes casos:

vetor_aleatorio.txt → números em ordem aleatória.

vetor_ordenado.txt → números em ordem crescente.

vetor_inverso.txt → números em ordem decrescente (pior caso do QuickSort clássico).

vetor_repetidos.txt → vetor com muitos elementos repetidos.

Cada vetor possui 1000 elementos.

===Estrutura do Repositório===

Letra-A.py → Implementação do QuickSort recursivo.

Letra-B.py → QuickSort híbrido (com busca empírica do melhor M).

Letra-C.py → QuickSort híbrido com técnica da mediana-de-três.

gerador_numeros.py → gera as massas de teste (.txt).

Arquivos .txt → vetores de entrada para os experimentos.
