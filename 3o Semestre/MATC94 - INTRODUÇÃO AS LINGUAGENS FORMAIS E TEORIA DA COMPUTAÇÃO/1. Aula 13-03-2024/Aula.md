# A matemática entre a entidade e a representação

|Entididade|Modelo Matemático|Representação|
|----------|-----------------|-------------|
|Mês       |Número inteiro no intervalo [1,12]| Um dos Caracteres 1,2,3,4,5,6,7,8,9,0, A ou B|
|Remuneração| Número Real Positivo| Número real na base 10|
|Presença| Vetor de números, um para cada dia do mês | Sequência de números reais na base 10|
|FP| Relação |Tabela em que cada linha tem o nome, cargo, salário, etc.|
|Cálculo de FP| Algoritmo| Programa|

# Representações múltiplas

|Representações para mês | Símbolos |
|------------------------|----------|
|Janeiro, fevereiro, ... , dezembro | Letras a, b, ..., z|
|Numerais na base decimal | Dígitos 0 a 9|
|Numerais na base binária | Dígitos 0 e 1|
|Numerais em algarismos romanos | Letras I, V e X|
|Sequências de uma doze 0s | Apenas o dígito 0|

- Cada conjunto é uma linguagem em que cada sequência de símbolos representa uma forma de demonstrar os meses

# Linguagens formais

- Computadores precisam de somandos simples e diretos
- Definidos por meio de regras sem ambiguidade
    - Programa -> Lista de comandos
    - Comando -> Leia, imprima, faça, repita, se...
- Com um conjunto de regras é possível analisar um programa e dividi-lo em seus blocos
    - Leia x
    - Leia y
    - Faça z < x + y 
    - Imprima z

# Máquinas Universais e Computabilidade

- Modelos matemáticos que representam computadores
- Não se preocupam com a eficiência dos programas, apenas com o que podem ou não fazer
- Qual é o melhor computador concebível?
    - Velocidade infinita
    - Memória infinita
- Computabilidade não se preocupa com eficiência
- O Computador faz? descubrimos primeiro, depois como fazer melhor
- Caixeiro Viajante - é computável? tem solução?