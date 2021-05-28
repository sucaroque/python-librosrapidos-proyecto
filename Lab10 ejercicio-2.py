#Formato de colores para no estar escribiendo cada codigo, para que sea mas facil de reconocer con nombres he usado pildora 1
azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva="\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
rojo,rosado,azul,verde,cyan,fin="\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"

#========================================== Ininio pregunta 2.1 =====================================================
print(azul_oscuro_blanco+"Solución Laboratorio 10 - ejercicio 2.1"+fin)
codigo_apellido_alumno={20211:"Castillo Terrones",20212:"Cerrón Rojas",20213:"Fujimori Inomoto",20214:"Montesinos Torres",20215:"Velazco Alvarado"}
codigo = codigo_apellido_alumno.get(1,"No esiste")
print(rojo+"Codigo\t Apellidos"+fin)
for clave in codigo_apellido_alumno:
  print(clave,"\t",codigo_apellido_alumno[clave])
#========================================== Fin pregunta 2.1 ========================================================

#========================================== Ininio pregunta 2.2 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.2"+fin)
print("Cantidad de alumnos son:",len(codigo_apellido_alumno))
#========================================== Fin pregunta 2.2 ========================================================

#========================================== Ininio pregunta 2.3 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.3"+fin)
print(rojo+"Claves"+fin)
for key in codigo_apellido_alumno:
  print (key)
#========================================== Fin pregunta 2.3 ========================================================

#========================================== Ininio pregunta 2.4 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.4"+fin)
print(rojo+"Valores"+fin)
for key in codigo_apellido_alumno:
  print (codigo_apellido_alumno[key])
#========================================== Fin pregunta 2.4 ========================================================

#========================================== Ininio pregunta 2.5 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.5"+fin)
codigos=codigo_apellido_alumno.keys()
print(f"Elija un código del alumno que se muestra {rojo}aquí {fin}{codigos}:", end=" ")
codigo=int(input())
mostrar_codigo = codigo_apellido_alumno.get(codigo, f'NO EXISTE CÓDIGO {codigo}')
print(rojo+"El valor del elemento dada la clave es:"+fin,mostrar_codigo)
#========================================== Fin pregunta 2.5 ========================================================

#========================================== Ininio pregunta 2.6 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.6"+fin)
print(f"Ingrese el código del nuevo alumno:", end=" ")
codigo1=int(input())
print(f"Ingrese los apellidos del nuevo alumno:", end=" ")
apellido1=input()
codigo_apellido_alumno[codigo1] =apellido1
#========================================== Fin pregunta 2.6 ========================================================

#========================================== Ininio pregunta 2.7 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.7"+fin)
print("El diccionario con el nuevo alumno es:")
print(rosado+"Codigo\t Apellidos"+fin)
for clave in codigo_apellido_alumno:
  print(clave,"\t",codigo_apellido_alumno[clave])
#========================================== Fin pregunta 2.7 ========================================================

#========================================== Ininio pregunta 2.8 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.8"+fin)
print('Agregamos datos del nuevo alumno al diccionario utilizango la función '+cursiva+'"setdefault"'+fin)
print(f"Ingrese el código del nuevo alumno:", end=" ")
codigo2=int(input())
print(f"Ingrese los apellidos del nuevo alumno:", end=" ")
apellido2=input()
codigo_apellido_alumno.setdefault(codigo2, apellido2)
print("El diccionario con el nuevo alumno es:")
print(verde+"Codigo\t Apellidos"+fin)
for clave in codigo_apellido_alumno:
  print(clave,"\t",codigo_apellido_alumno[clave])
#========================================== Fin pregunta 2.8 ========================================================

#========================================== Ininio pregunta 2.9 =====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.9"+fin)
print('Eliminamos un elemento del diccionario')
codigos_final=codigo_apellido_alumno.keys()
print(f"Elija un código del alumno para eliminar, de la lista que se muestra {rojo}aquí {fin}{codigos_final}:", end=" ")
codigo3=int(input())
elimina_dato=codigo_apellido_alumno.pop(codigo3, f'NO EXISTE CÓDIGO{codigo3}')
print("El diccionario con el nuevo alumno eliminado es:")
print(azul+"Codigo\t Apellidos"+fin)
for clave in codigo_apellido_alumno:
  print(clave,"\t",codigo_apellido_alumno[clave])
#========================================== Fin pregunta 2.9 ========================================================

#========================================== Ininio pregunta 2.10 ====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.10"+fin)
print('Realizamos una copia del diccionario')
lista_alumnos = codigo_apellido_alumno.copy()
#========================================== Fin pregunta 2.10 =======================================================

#========================================== Ininio pregunta 2.11 ====================================================
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 2.11"+fin)
print('Eliminamos los elementos del diccionario')
codigo_apellido_alumno.clear()
#========================================== Fin pregunta 2.11 =======================================================