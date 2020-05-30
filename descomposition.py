class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'stand_by'
        self._engine = Engine(cilindres=4)

    def acelerate(self):
        self._engine.inyect_gasoil(10)
        self._status = 'going'


class Engine:
    def __init__(self, cilindres, tipe='gasoil'):
        self.cilindres = cilindres
        self.tipe = tipe
        self._temperature = 0

    def inyect_gasoil(self, liters):
        print()
