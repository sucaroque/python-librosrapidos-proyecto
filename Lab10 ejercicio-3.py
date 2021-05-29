#Formato de colores para no estar escribiendo cada codigo, para que sea mas facil de reconocer con nombres he usado pildora 1
azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva="\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
rojo,rosado,azul,verde,cyan,fin="\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 3"+fin)
bucle="1"
usuarios={}
while bucle!="0":
   print('\n'+rosado+'MENU DE OPCIONES'+fin)
   print(rosado+'Para continuar presione 1:'+fin)
   print(rosado+'Para salir presione \t0:'+fin)
   bucle=input('Ingrese una opción:')
   if bucle=="1":
     print("\n"+azul_oscuro_blanco+"REGISTRO DE USUARIOS"+fin)
     print("Ingrese el e-mail del usuario:", end=" ")
     email=input()
     print("Ingrese la contraseña del usuario:", end=" ")
     password=input()
     usuarios.setdefault(email, password)
     
   elif bucle=="0":
     break
   elif bucle!="1":
     print('Has ingresado opción incorrecto')
     continue
print("\nEl diccionario con el nuevo usuario es:")
print(verde+"Correo\t\t\t\t Password"+fin)
for clave in usuarios:
  print(clave,"\t\t",usuarios[clave])