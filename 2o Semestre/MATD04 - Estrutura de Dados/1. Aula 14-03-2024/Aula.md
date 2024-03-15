# Algoritimos

- Definição:
Pode ser definido como uma sequência __finita__ de __instruções__ que descrevem uma __solução__ para um __problema__.

- Um algoritimo:
1. Possui um conjunto de entrada
2. Possui um conjunto de saída
3. Possui, associada a ele, um __modelo computacional__ que define o __conjunto de instruções__ usados no algoritimo e um __custo associado__ a casa uma delas
4. É um procedimento __finito__

- EXEMPLO DO PROBLEMA: Ordenação

    - ENTRADA: <br>
    Arranjo [a1, a2 ... an] de n números inteiros n >= 1 
    - SAÍDA: <br>
    Permutação [a1'. a2' ... an'] de n números inteiros igual da entrada tal que a a1' =< a2' ... =< an'
    - ALGORITIMO: <br>
    Ordenação Por Inserção
    A: Arranjo A[a1 ... an] de n números inteiros n >= 1
    Obs. O primeiro Index é 1

    ```
    for j <- 2 to n do
        chave <- A[j]
        i <- j - 1

        while (i > 0) and (A[i] > chave) do
            A[i + 1] <- A[i]
            i <- i - 1
        A[i+1] <- chave
    ```

    - EXEMPLO:
    Obs. O primeiro Index é 0
    ```
    A: [10, 25, 15, 5]
    j = 0 - FOR - ARRANJO = [10, 25, 15, 5]
    j = 0 - FIM FOR - ARRANJO = [10, 25, 15, 5]
    j = 1 - FOR - ARRANJO = [10, 25, 15, 5]
    j = 1 - FIM FOR - ARRANJO = [10, 25, 15, 5]
    j = 2 - FOR - ARRANJO = [10, 25, 15, 5]
    j = 2 - WHILE i = 0 - CHAVE = 15 - ARRANJO = [10, 25, 25, 5]
    j = 2 - FIM FOR - ARRANJO = [10, 15, 25, 5]
    j = 3 - FOR - ARRANJO = [10, 15, 25, 5]
    j = 3 - WHILE i = 1 - CHAVE = 5 - ARRANJO = [10, 15, 25, 25]
    j = 3 - WHILE i = 0 - CHAVE = 5 - ARRANJO = [10, 15, 15, 25]
    j = 3 - WHILE i = -1 - CHAVE = 5 - ARRANJO = [10, 10, 15, 25]
    j = 3 - FIM FOR - ARRANJO = [5, 10, 15, 25]
    ```