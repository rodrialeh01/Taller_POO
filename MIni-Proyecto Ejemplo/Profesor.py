class Profesor():
    def __init__(self, id, nombre, dpi):
        self.id = id
        self.nombre = nombre
        self.dpi = dpi

    def getId(self):
        return self.id

    def getDpi(self):
        return self.dpi

    def getNombre(self):
        return self.nombre

    def setId(self, id):
        self.id = id

    def setDpi(self,dpi):
        self.dpi = dpi

    def setNombre(self, nombre):
        self.nombre = nombre