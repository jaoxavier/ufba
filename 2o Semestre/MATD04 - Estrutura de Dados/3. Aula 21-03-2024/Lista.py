class Lista:

    def __init__(self, nMax):
        self.nMax = nMax
        self.dados = [0] * nMax 
        self.nElems = 0

    def consultar(self, x):
        for i in range(self.nElems):
            if self.dados[i] == x:
                return True
        return False

    def insercao(self, x):
        if self.nElems < self.nMax:
            self.dados[self.nElems] = x
            self.nElems += 1
            return
        print("Lista Cheia")        

    def remocao(self, x):
        for i in range(self.nElems):
            if self.dados[i] == x:
                self.dados[i] = self.dados[self.nElems-1]
                self.nElems -= 1
                return
        print("Valor não encontrado")
                
l = Lista(3)

l.insercao(1)
l.insercao(3)
l.insercao(5)
l.insercao(7) # Lista Cheia

print(l.consultar(3))
l.remocao(5)   
l.remocao(3467) # Valor Não encontrado
print(l.consultar(7))

for i in range(l.nElems):
    print(l.dados[i]) # Só deve aparecer dois elementos

print("###")

l.insercao(5)

for i in range(l.nElems):
    print(l.dados[i]) # Deve aparecer os três elementos
