azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva=\
"\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
cielo,rojo,rosado,azul,verde,cyan,fin=\
"\033[1;36m","\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(cielo+"LABORATORIO 15 - EJERCICIO 2.6"+fin)
class Rectangulo:
  def __init__(self,l,a):
     self.largo=l
     self.ancho=a
  
  def perimetro(self):
     p=2*self.largo+2*self.ancho
     return p
  def area(self):
     a=self.largo*self.ancho
     return a
  def diagonal(self):
     d=(self.largo**2+self.ancho**2)**0.5
     return d
ilargo=int(input("Ingrese largo del rectángulo:"))
iancho=int(input("Ingrese ancho del rectángulo:"))
rect1=Rectangulo(ilargo,iancho)
print(rosado+"PERIMETRO:"+fin,rect1.perimetro())
print(rosado+"AREA\t:"+fin,rect1.area())
print(rosado+"DIAGONAL:"+fin,rect1.diagonal())
print(rosado+"LARGO\t:"+fin,rect1.largo)
print(rosado+"ANCHO\t:"+fin,rect1.ancho)