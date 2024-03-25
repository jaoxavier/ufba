# Listas

- Conjunto de elementos
- Elemento: Conjunto de atributos, sendo o principal de um elemento a sua chave, que serve de identificador do elemento

## Elaboração

- Quando criamos a lista, ele se parece com isso
- |0|0|0|0|0|0|0|0|
- Nenhuma inserção foi feita, logo, se fosse buscar algum número dentro dessa lista, incluindo o zero, deve retornar FALSE
- Porém, se pesquisarmos 0, retornará True, afinal tem elementos de valor 0 na lista
- Para que isso não aconteça, precisamos definir a quantidade de elementos que já foram inseridos, assim, não será consultado valores que não forem inseridos
- Vamos supor que inserimos um Zero e o números de Elementos passa a ser 1
- Então vamos ler o primeiro elemento da lista, que retornará TRUE, afinal, o primeiro é ZERO
- Se o número de elementos for 0, retornará FALSE, afinal, não correu por nenhum elemento

## Criação de uma lista

```python
class Lista:

    def __init__(self, nMax): # Aqui definimos o tamanho máximo da lista
        self.dados = [0] * nMax # Aqui criamos o array com o tamanho definido da lista com X elementos 0
        self.nElems = 0 # Aqui definimos a quantidade de elementos inseridos
    
    def consultar(self, x):
        for i in range(self.nElems): # Fazemos com que o for percorre entre o primeiro elemento e a quantidade de elementos que contém
            if self.dados[i] == x:
                return True
        return False

    def insercao(self, x):
        if self.nElems < self.nMax: # Verificamos se a quantidade de elementos na lista
            self.dados[self.nElems] = x # Adicionamos na lista
            self.nElems += 1 # Aumentamos a quantidades de elementos lidos
            return
        print("Lista Cheia")        

    def remocao(self, x):
        for i in range(self.nElems):
            if self.dados[i] == x: # Achamos o elemento na lista
                self.dados[i] = self.dados[self.nElems-1] # Colocamos o último elemento da lista no lugar do excluido
                self.nElems -= 1 # Diminuimos a quantidade de elementos lidos
                return
        print("Valor não encontrado")
         
```