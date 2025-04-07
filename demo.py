class Cuadrado:
    def __init__(self, lado):
        self.lado = lado 
        
    def area (self):
         return self.lado **2 
        
        
lado1 = int(input("Ingresa un lado: "))
mi_cuadrado= Cuadrado(lado1)
print("el area del cuadrado es: ", mi_cuadrado.area())