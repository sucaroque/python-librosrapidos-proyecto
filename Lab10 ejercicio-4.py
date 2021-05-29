#Formato de colores para no estar escribiendo cada codigo, para que sea mas facil de reconocer con nombres he usado pildora 1
azul_claro_blanco,purpura_blanco,azul_oscuro_blanco,cursiva="\033[1;97;44m","\033[1;97;45m","\033[1;97;46m","\033[3;1;30m"
rojo,rosado,azul,verde,cyan,fin="\033[1;91m","\033[1;95m","\033[1;94m","\033[1;92m","\033[1;96m","\033[0m"
print(azul_oscuro_blanco+"\nSolución Laboratorio 10 - ejercicio 4"+fin)
bucle="1"
clientes={}
while bucle!="6":
   print('\n'+rosado+'*** MENU DE OPCIONES ***'+fin)
   print(rosado+'1. Registrar clientes'+fin)
   print(rosado+'2. Mostrar clientes'+fin)
   print(rosado+'3. Buscar clientes'+fin)
   print(rosado+'4. Actualizar clientes'+fin)
   print(rosado+'5. Eliminar clientes'+fin)
   print(rosado+'0. Salir\t'+fin)
   bucle=input('Ingrese una opción(del 0-5):')
   if bucle=="1":
     print("\n"+azul_oscuro_blanco+"REGISTRO DE CLIENTES"+fin)
     print("Ingrese RUC de la empresa:", end=" ")
     ruc=input()
     print("Ingrese nombre de la empresa:", end=" ")
     empresa=input()
     clientes.setdefault(ruc, empresa)
   elif bucle=="2":
     print("\n========= EMPRESAS REGISTRADOS ========")
     print(verde+"RUC\t\t\t Nombre empresa"+fin)
     for clave in clientes:
       print(clave,"\t\t",clientes[clave])
   elif bucle=="3":
     codigos=clientes.keys()
     print(f"Ingresa RUC de la empresa a buscar:", end=" ")
     codigo=input()
     mostrar_codigo = clientes.get(codigo, f'NO FIGURA LA EMPRESA {codigo}')
     print(rojo+"La empresa es:"+fin,mostrar_codigo)
   elif bucle=="4":
     print(f"Ingresa RUC de la empresa para actualizar:", end=" ")
     ruc1=input()
     mostrar_codigo = clientes.get(ruc1, f'NO FIGURA LA EMPRESA {ruc1}')
     for clave,valor in clientes.items():
       if clave == ruc1:
         print("La empresa encontrada es ===> ", end=" ")
         print(clave,clientes[clave])
         nombre_empresa=input("Ingresa el nuevo nombre de la empresa")
         clientes[clave] = nombre_empresa
         break
   elif bucle=="5":
     print('Eliminar una empresa')
     codigos_final=clientes.keys()
     print(f"Ingresa RUC de la empresa a eliminar", end=" ")
     codigo2=input()
     for clave,valor in clientes.items():
       if clave == codigo2:
         print("Eliminando a la empresa ===>",end=" ")
         print(clave,clientes[clave])
         break
     mostrar = clientes.get(codigo2, f'NO FIGURA LA EMPRESA CON RUC {codigo2}')
     elimina_dato=clientes.pop(codigo2, f'NO EXISTE RUC{codigo2}')
   elif bucle=="0":
     break
   elif bucle!="1":
     print('Has ingresado opción incorrecto')
     continue