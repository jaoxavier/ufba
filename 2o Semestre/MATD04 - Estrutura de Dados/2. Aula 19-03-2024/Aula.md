# Indução no algoritimo

- OrdenaçãoPorInserção(A, n) - Criada na semana passada
- Utilizaremos o mesmo algoritimo para testar se esse algoritimo é válido em qualquer A

## Base da indução (j = 2)
## Casos:

1. a1 < a2
    1. Para esse caso A: [a1, a2]
    2. Quando o algoritimo chegar no while e testar se A[i] (a1) é maior que a chave (a2) vai ser FALSO
    3. Logo, não entrará no while e A[i+1] = chave
    4. Logo o array A vai ser A: [a1, a2]
    5. Logo, a ordenação funciona

2. a1 > a2
    1. Para esse caso A: [a1, a2]
    2. Quando o algoritimo chegar no while e testar se A[i] (a1) é maior que a chave (a2) vai ser VERDADEIRO
    3. Logo, entrará no WHILE e copiará o elemento
    4. O array ficará A: [a2, a2]
    5. Na segunda vez que for entrar no WHILE, o A[i] (a2) vai ser igual a chave, logo não entrará no while
    6. Assim, a chave será copiada e A: [a2, a1]
    5. Logo, a ordenação funciona

3. a1 = a2
    1. Para esse caso A: [a1, a2]
    2. Quando o algoritimo chegar no while e testar se A[i] (a1) é maior que a chave (a2) vai ser FALSO
    3. Logo, não entrará no while e A[i+1] = chave
    4. Logo o array A vai ser A: [a1, a2]
    5. Logo, a ordenação funciona

## Agora o PASSO da INDUÇÃO (J = k + 1)
## Casos:

A: [a1, a2, a3 ... ak-1, ak, ak+1 ... an]

1. ak+1 >= ak (ficará no final)
    1. Para esse caso A: [a1, a2, a3 ... ak-1, ak, ak+1]
    2. Quando o algoritimo chegar no while e testar se A[i] (a1) é maior que a chave (a2) vai ser FALSO
    3. Logo, não entrará no while e A[i+1] = chave
    4. Logo o array A vai ser A: [a1, a2, a3 ... ak-1. ak, ak+1]
    5. Logo, a ordenação funciona

2. ak+1 < a1 (ficará no inicio)
    1. Para esse caso A: [a1, a2, a3 ... ak-1, ak, ak+1]
    2. Quando esse algoritimo chegar no WHILE e testar se A[i] (ak) é maior que a chave (ak+1) vai ser VERDADEIRO
    3. Logo entrará no while e copiará A: [a1, a2, a3 ... ak-1, ak, ak]
    4. Quando esse algoritimo chegar pelo WHILE na segunda vez e testar se A[i] (ak-1) é maior que a chave (ak+1) vai ser VERDADEIRO
    5. Logo entrará no while e copiará A: [a1, a2, a3 ... ak-1, ak-1, ak]
    6. Isso se repetirá até chegar no primeiro elemento
    7. A: [a1, a1, a2, a3 ... ak-2, ak-1, ak]
    8. Agora, o A[i] não será maior que a chave, portanto, sairá do WHILE
    9. A chave será copiada e assim, A: [ak+1, a1, a2, a3 ... ak-2, ak-1, ak]
    10. Logo, a ordenação funciona

3. ai =< ak+1 < ak (ficará no meio)
    1. Para esse caso A: [a1, a2, a3 ... ai, ak-1, ak, ak+1]
    2. Quando esse algoritimo chegar no WHILE e testar se A[i] (ak) é maior que a chave (ak+1) vai ser VERDADEIRO
    3. Logo entrará no while e copiará A: [a1, a2, a3 ... ai, ak-1, ak, ak] 
    4. Quando esse algoritimo chegar pelo WHILE na segunda vez e testar se A[i] (ak-1) é maior que a chave (ak+1) vai ser VERDADEIRO
    5. Logo entrará no while e copiará A: [a1, a2, a3 ... ai, ak-1, ak-1, ak]
    6. Quando esse algoritimo chegar pelo WHILE na segunda vez e testar se A[i] (ai) é maior que a chave (ak+1) vai ser FALSO
    7. Assim, a chave vai ser copiada, e A: [a1, a2, a3 ... ai, ak+1, ak-1, ak]
    8. Logo, a ordenação funciona
 
