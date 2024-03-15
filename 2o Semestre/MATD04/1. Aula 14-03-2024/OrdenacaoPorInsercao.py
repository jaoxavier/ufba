A = [10, 25, 15, 5]

def OrdenacaoPorInsercao(A):
    print(f"A: {A}")

    for j in range(len(A)):
        print(f"j = {j} - FOR - ARRANJO = {A}")
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
            print(f"j = {j} - WHILE i = {i} - CHAVE = {key} - ARRANJO = {A}")
        A[i+1] = key
        print(f"j = {j} - FIM FOR - ARRANJO = {A}")
    return A

OrdenacaoPorInsercao(A)