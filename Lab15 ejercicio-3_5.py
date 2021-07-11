azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva=\
"\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
cielo,rojo,rosado,azul,verde,cyan,fin=\
"\033[1;36m","\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(cielo+"LABORATORIO 15 - EJERCICIO 3.5"+fin)
class Triangulo:
  def __init__(self,a,b,c):
     self.lado_a=a
     self.lado_b=b
     self.lado_c=c
  
  def perimetro(self):
     p=self.lado_a+self.lado_b+self.lado_c
     return p
  def area(self):
     s=self.perimetro()/2
     area=(s*(s-self.lado_a)*(s-self.lado_b)*(s-self.lado_c))**0.5
     return area

t=Triangulo(3,4,5)
print(rosado+"PERIMETRO:"+fin,t.perimetro())
print(rosado+"AREA\t:"+fin,t.area())