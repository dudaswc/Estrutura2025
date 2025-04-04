Problema: Programa de Mentoria para Mulheres na Tecnologia  

Descrição: Uma organização sem fins lucrativos criou um programa de mentoria para incentivar a participação de mulheres na tecnologia. 
O sistema precisa gerenciar a fila de mulheres que se inscrevem para receber mentoria, garantindo que elas sejam atendidas na ordem de chegada.
Cada participante entra na fila ao se inscrever, e uma mentora pode chamar a próxima candidata disponível para fazer a inscrição.

Requisitos:
✅ Implementar uma fila para armazenar as participantes que aguardam mentoria.
✅ Adicionar uma participante à fila.
✅ Remover a participante mais antiga da fila quando for chamada para mentoria (FIFO).

# Classe para armazenar participantes da mentoria usando um array dinâmico
class PersonalArray:
    SIZE = 5

    def __init__(self):
        self.insertPosition = 0
        self.elements = [None] * self.SIZE

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return self.insertPosition
    
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    def clear(self):
        self.elements = [None] * self.SIZE
        self.insertPosition = 0
    
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:
            self.elements[index] = self.elements[index + 1]
            index += 1
        self.elements[self.insertPosition - 1] = None
        self.insertPosition -= 1
        return removedElement
    
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1
    
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]


# Implementação da fila para o programa de mentoria
class MentoriaQueue:
    def __init__(self):
        self.list = PersonalArray()

    # Adiciona uma participante no final da fila
    def inscrever_participante(self, nome):
        self.list.append(nome) 
        print(f"{nome} foi inscrita na mentoria.")

    # Remove a participante mais antiga (FIFO)
    def chamar_para_mentoria(self):
        if self.list.isEmpty():
            print("Nenhuma participante na fila.")
            return None
        participante = self.list.removePosition(0)  
        print(f"Chamando {participante} para a mentoria.")
        return participante


# Criando uma instância da fila de mentoria
mentoria = MentoriaQueue()

# Inscrevendo participantes
mentoria.inscrever_participante("Mariana")
mentoria.inscrever_participante("Carla")
mentoria.inscrever_participante("Fernanda")
mentoria.inscrever_participante("Ana")
mentoria.inscrever_participante("Beatriz")

# Chamando participantes para mentoria 
print(mentoria.chamar_para_mentoria())  # Mariana
print(mentoria.chamar_para_mentoria())  # Carla
print(mentoria.chamar_para_mentoria())  # Fernanda
print(mentoria.chamar_para_mentoria())  # Ana
print(mentoria.chamar_para_mentoria())  # Beatriz


