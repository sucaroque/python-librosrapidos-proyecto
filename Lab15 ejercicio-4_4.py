azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva=\
"\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
cielo,rojo,rosado,azul,verde,cyan,fin=\
"\033[1;36m","\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(cielo+"LABORATORIO 15 - EJERCICIO 4.4"+fin)
class Cuadrado:
  def __init__(self,a):
     self.lado=a
  
  def perimetro(self):
     p=4*self.lado
     return p
  def area(self):
     s=self.perimetro()/2
     area=self.lado**2
     return area
  def diagonal(self):
     d=self.lado*(2)**0.5
     return d
ilado=float(input("Ingrese lado del cuadrado:"))
cuad=Cuadrado(ilado)
print(cyan+"PERIMETRO:"+fin,cuad.perimetro())
print(cyan+"AREA\t:"+fin,cuad.area())
print(cyan+"DIAGONAL:"+fin,cuad.diagonal())