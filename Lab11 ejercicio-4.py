#LABORATORIO 11 - EJERCICIO 4
from datetime import datetime
from datetime import timedelta
#Formato de colores para no estar escribiendo cada codigo, para que sea mas facil de reconocer con nombres he usado pildora 1
azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva="\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
rojo,rosado,azul,verde,cyan,final="\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(azul_oscuro_blanco+"\nSolución Laboratorio 11 - ejercicio 4"+final)

inicio = datetime(2021, 1, 1)
fin = datetime(2021, 6, 5)
dias = (fin - inicio).days + 1
fechas = []

contador=0
for i in range(dias):#generamos el intervalo de fechas y almacenamos en la lista fechas
	fechas.append(inicio+timedelta(i))

for fecha in fechas:#Para recorrer las fechas de la lista
  if ((fecha.weekday())==6):#Para capturar los dias domingos en la lista fechas
    contador +=1

inicio_formato=inicio.strftime("%d %b %Y")
fin_formato=fin.strftime("%d %b %Y")
print(f"En el intervalo del \"{rosado+inicio_formato+final}\" al \"{rosado+fin_formato+final}\" hay",contador,"Domingos")