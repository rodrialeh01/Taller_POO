class Estudiante():
    def __init__(self, id, dpi, nombre, carrera):
        self.id = id
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.cursos = []

    def getId(self):
        return self.id

    def getDpi(self):
        return self.dpi

    def getNombre(self):
        return self.nombre

    def getCarrera(self):
        return self.carrera

    def setId(self, id):
        self.id = id

    def setDpi(self,dpi):
        self.dpi = dpi

    def setCarrera(self, carrera):
        self.carrera = carrera

    def setNombre(self, nombre):
        self.nombre = nombre