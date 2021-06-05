#LABORATORIO 11 - EJERCICIO 3
from datetime import datetime
#Formato de colores para no estar escribiendo cada codigo, para que sea mas facil de reconocer con nombres he usado pildora 1
azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva="\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
rojo,rosado,azul,verde,cyan,final="\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(azul_oscuro_blanco+"\nSolución Laboratorio 11 - ejercicio 3"+final)

inicio = datetime(2021, 6, 1)
fin = datetime(2021, 6, 5)
dias = (fin - inicio).days

inicio_formato=inicio.strftime("%d %b %Y")#Formatea la fecha inicio
fin_formato=fin.strftime("%d %b %Y")#Formatea la fecha final
print(f"La diferencia entre \"{verde+inicio_formato+final}\" y \"{verde+fin_formato+final}\" es",dias,"Dias")