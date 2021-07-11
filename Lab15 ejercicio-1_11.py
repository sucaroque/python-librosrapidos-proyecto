azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva=\
"\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
cielo,rojo,rosado,azul,verde,cyan,fin=\
"\033[1;36m","\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(cielo+"LABORATORIO 15 - EJERCICIO 1.11"+fin)
class Aritmetica:
  def __init__(self,aa,bb):
     self.a=aa
     self.b=bb
  
  def suma(self):
     s=self.a+self.b
     return s
  def resta(self):
     r=self.a-self.b
     return r
  def producto(self):
     p=self.a*self.b
     return p
  def cociente(self):
     c=self.a/self.b
     return c
  def residuo(self):
     rd=self.a%self.b
     return rd
  def potencia(self):
     pt=self.a**self.b
     return pt
precios=Aritmetica(18,13)
print(purpura_blanco+"SUMA:"+fin,precios.suma())
print(purpura_blanco+"RESTA:"+fin,precios.resta())
print(purpura_blanco+"COCIENTE:"+fin,precios.cociente())
print(purpura_blanco+"RESIDUO:"+fin,precios.residuo())
