class Fila:

        def __init__(self):
            self._items = []

        def enqueue(self, item): #Enfileirar (adiciona um dado no início da lista)
            if item == None:
                raise ValueError("Item nao pode ser None")
            
            self._items.insert(0, item)

        def dequeue(self): #Desenfileirar (remove o ultimo dado da lista)
            if self.is_empty():
                raise IndexError("Fila está vazia")
            
            return self._items.pop()

        def front(self): #Primeiro da Fila (ultimo dado da lista)
            if self.is_empty():
                raise IndexError("Fila está vazia")
            
            return self._items[-1]
        
        def is_empty(self): #Verifica se a Fila esta vazia
            return len(self._items) == 0
        
        def size(self): #Retorna o tamanho da Fila
            return len(self._items)
        
        def __str__(self):
            return str(self._items)
        
        def get_items(self):
            return self._items