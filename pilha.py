class Pilha:

    def __init__(self):
        self._items = []

    
    def push(self, item):
        self._items.append(item) 

    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")

        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")

        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def clear(self):
        self._items = []