class leer:
    def __init__(self, fichero):
        f = open(fichero, 'r')
        lista = []
        self.f = f
        self.lista = lista
    
    def crear_lista(self):
        for i in self.f:
            i = i.rstrip('\n')
            columna = i.split(',')
            self.lista.append(columna)
