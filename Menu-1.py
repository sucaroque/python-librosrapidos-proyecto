from IPython.display import clear_output 
import time
 #===============Formato de colores para no estar escribiendo cada codigo,===============
azul_claro_blanco,negro_fondo,purpura_blanco,azul_oscuro_blanco,cursiva,\
amarillo_fondo,rojo_fondo,verde_fondo,violeta_fondo=\
    "\033[1;97;44m","\033[1;40m","\033[1;97;45m","\033[1;97;46m",\
    "\033[3;1;30m","\033[1;43m","\033[1;41m","\033[1;42m","\033[1;45m"
amarillo,rojo,rosado,azul,verde,cyan,negro,blanco,violeta=\
    "\033[1;93m","\033[1;31m","\033[1;95m","\033[1;94m","\033[1;92m",\
    "\033[1;96m","\033[1;30m","\033[1;97m","\033[1;95m"
subrayado,bordes,fin="\033[1;4m","\033[1;51m","\033[0m"
#======================para que sea mas facil de reconocer con nombres===================

aplicaciones=True
while aplicaciones:  #=============MIENTRAS QUE APLICAMOS SEA VERDADERA==================

#=======================EL BUCLE DEL MENU PRINCIPAL SE VA REPETIR=========================
    print ('\033[1;36m'+"+------------------------------------------------------+")
    print ('\033[1;36m'+"¦                  PROYECTO FINAL                      ¦")
    print ('\033[1;36m'+"¦------------------------------------------------------¦")
    print ('\033[1;36m'+"¦MENU DE APLICACIONES                                  ¦")
    print ('\033[1;36m'+"¦1.DISCORD                                             ¦")
    print ('\033[1;36m'+"¦2.CALENDARIO                                          ¦")
    print ('\033[1;36m'+"¦3.CALCULADORA                                         ¦")
    print ('\033[1;36m'+"¦4.TELEFONO                                            ¦")
    print ('\033[1;36m'+"¦0.SALIR DEL MENU                                      ¦")
    print ('\033[1;36m'+"+------------------------------------------------------+")
#=======================EL BUCLE DEL MENU PRINCIPAL SE VA REPETIR=========================
    borrarPantalla = lambda: os.system ("cls")
    borrarPantalla() #Limpia la pantalla
    apli=input("\n"+bordes+verde+"SELECCIONA UNA APLICACION--> :"+fin)
    cod=["1","2","3","4","0"]   #=======MUY IMPORTANTES LAS LISTAS DE VALORES ALMACENADOS EN COD========
    time.sleep(0)
    clear_output()
    if apli not in cod:  #==========SI LO QUE SE INGRESO EN APLID NO ESTA EN LA LISTA COD===============
        print(rojo+"LA OPCION ELEGIDA ES INVALIDA"+fin)

    if apli=="0":
        aplicaciones = False

#===============================================OPCION 1 HACE LLAMADO A DISCORD=========================================
    if apli == "1":

        personas={"Haru":3114,"Nova":3248,"Zenie":5234}
        opciones =True
        while opciones:
#==============================SUB MENU DE DISCORD========================
            print(subrayado+azul+"DISCORD"+fin)
            print('\n'+subrayado+cyan+ '* MENU DE OPCIONES *' + fin)
            print("\n"+bordes+amarillo+"1.Amigos")
            print("2.Agregar nuevos amigos")
            print("3.Buscar Amigos")
            print("4.Eliminar de amigos")
            print("0.Salir.")
            print("------------------------"+fin)
#==============================SUB MENU DE DISCORD========================

            codigos=["1","2","3","4","0"]
            elige=input("\n"+blanco+"elige una opcion:----->"+fin)

            if elige not in codigos:
                print(rojo+subrayado+"LA OPCION ELEGIDA ES INVALIDA"+fin)
                print("")
            if elige=="1":
                print("\n"+subrayado+rosado+"LISTA DE AMIGOS"+fin)
                for g in personas:

                    print(g,":",personas[g])
            if elige=="2":
                print("\n"+subrayado+rosado+"AGREGAR AMIGOS"+fin)
                agregar=input(azul+"Nombre del usuario: "+fin)
                if agregar in personas:
                    print("\n"+agregar,amarillo,subrayado,"ya esta en lista de amigos"+fin+"\n")
                else:
                    etiqueta=input(azul+"Ingresa su etiqueta: "+fin)
                    personas[agregar]=etiqueta
                    print("\n"+amarillo+"felicidades!!"+fin,negro+agregar,fin+violeta+"ahora es tu nuevo amigo"+fin+"\n")
            if elige=="3":
                print("\n"+subrayado+rosado+"BUSCAR AMIGOS"+fin)

                opi = True
                buscar = input(cyan+"bucar a :"+fin)
                while opi:

                    if buscar not in personas:
                        print("\n"+rojo_fondo+bordes+ buscar, "no esta en tu lista de amigos"+fin)

                        print("\n"+amarillo+subrayado+"presiona 1  para agregar ala lista de tus amigos y 0 para salir de busqueda"+fin)
                        numeros = ["1", "0"]
                        ele = input("\n"+verde_fondo+"elige una opcion: "+fin)

                        if ele not in numeros:
                            print(bordes+rojo+"LA OPCION ELEGIDA ES INVALIDA"+fin)

                        if ele=="1":
                            etiqueta=input(violeta+"Ingresa su etiqueta: "+fin)
                            personas[buscar]=etiqueta
                            print("\n"+amarillo+"felicidades!!"+fin,negro+ buscar, fin+violeta+"ahora es tu nuevo amigo"+fin)
                        if ele=="0":
                            opi=False

                    else:
                        etiqueta=personas[buscar]
                        print("\n"+verde+"Usuario:"+fin,buscar)
                        print(verde+"Etiqueta:"+fin, personas[buscar])
                        opi=False
            if elige == "4":
                print("\n"+subrayado+rosado+"ELIMINAR DE LISTA DE AMIGOS"+fin)
                nombre=input(azul+"Igresa el nombre: "+fin)
                if nombre not in personas:
                    print("\n"+bordes+rojo_fondo+nombre,"no encontrado en tu lista de amigos"+fin+"\n")
                else:
                    del personas[nombre]
                    print(nombre,rojo+subrayado+"ha sido eliminado de tu lista de amigos"+fin+"\n")

            if elige=="0":
                opciones=False
#=====================================================FIN DE DISCORD====================================================

#=======================================OPCION 2 HACE LLAMADO AL CALENDARIO=============================================
    if apli =="2":
        import calendar   #=======EL IMPORT CALENDAR SE USA PARA HACER EL LLAMADO DEL CALENDARIO=====
        c = calendar.TextCalendar(calendar.SUNDAY)
        c.prmonth(2021, 7,5)  #===========AL PONER ELLO NOS MOSTRARA EL MES ACTUAL
        print()
        y=input(bordes+violeta_fondo+blanco+"Pesiona ENTER para salir de calendario"+fin)
        print("")
#=============================================FIN DEL CALENDARIOO=======================================================

#=================================OPCION 3 HACE LLAMADO A LA CALCULADORA================================================
    if apli == "3":
        from calcu import *  #INVOCAMOS SE SE IMPORTE EL ANTERIOR ARCHIVO CREADO -CALCU.PY-
        opcionesde = True
        while opcionesde:
# ===========================SUB MENU DE LA CALCULADORA============================
            print(subrayado+azul+"CALCULADORA"+fin+"\n")
            print(subrayado + cyan + '* MENU DE OPCIONES *' + fin+"\n")
            print(bordes+amarillo+'Sumar -------------------->  S ')
            print('Restar ------------------->  R ')
            print('Multiplicar -------------->  M ')
            print('Dividir ------------------>  D ')
            print('SALIR--------------------->  0 ')
            print( "-------------------------------"+fin)
# ===========================SUB MENU DE LA CALCULADORA===============================
            letras=["S","R","M","D","0"]
            selector=input("\n"+blanco+"Elige una opcion:----->"+fin)

            if selector not in letras:
                print("\n"+rojo+"OPCION INVALIDA"+fin+"\n")

            if selector== "S" :
                print("\n"+bordes+azul_claro_blanco+blanco+"SUMA"+fin+"\n")
                sumar()

            elif selector== "R":
                print("\n"+bordes+azul_claro_blanco+blanco+"RESTA"+fin+"\n")
                restar()

            elif selector== "M":
                print("\n"+bordes+azul_claro_blanco+blanco+"MULTIPLICACION"+fin+"\n")
                multiplicar()

            elif selector== "D":
                print("\n"+bordes+azul_claro_blanco+blanco+"DIVISION"+fin+"\n")
                dividir()
                print()

            elif selector =="0":
                opcionesde=False
#============================================FIN DE LA CALCULADORA======================================================

#==========================================OPCION 4 HACE LLAMADO A CONTACTOS============================================
    if apli == "4":
        print('\033[1;36m'+subrayado+"CONTACTOS"+fin+'\033[1;m')

        bucle = "1"
        contactos = {}
        while bucle != "6":
#============================SUB MENU DE CONTACTOS====================================
            print('\n'+ azul+subrayado+'* MENU DE OPCIONES *' + fin)
            print("\n"+amarillo+bordes+ '1. Agregar Contactos')
            print('2. Ver Contactos')
            print('3. Buscar Contactos')
            print('4. Actualizar Contactos')
            print('5. Eliminar Contactos')
            print('0. Salir\t\t\t\t')
            print("------------------------" + fin)
#============================SUB MENU DE CONTACTOS====================================

            bucle = input("\n"+blanco+'Ingrese una opcion(del 0-5): ' + fin)
            if bucle == "1":
                print("\n"+azul_oscuro_blanco+bordes+"REGISTRO DE CONTACTO" + fin)
                print("\n"+azul+"Ingrese El Numero: ", end=" "+fin)
                ruc = input()
                print(azul+"Ingrese El Nombre: ", end=" "+fin)
                empresa = input()
                contactos.setdefault(ruc, empresa)
            elif bucle == "2":
                print(violeta+ "\n======== CONTACTOS REGISTRADOS =======" + fin)
                print(bordes+azul+ "NUMERO\t\t\t NOMBRE DE CONTACTO" + fin)
                for clave in contactos:
                    print(clave, "\t\t", contactos[clave])
            elif bucle == "3":
                codigos = contactos.keys()
                print(f"\n"+verde_fondo+blanco+"Ingresa Numero a Buscar: ", end=" "+fin)
                codigo = input()
                mostrar_codigo = contactos.get(codigo, f'NO ESTA EN TUS CONTACTOS {codigo}')
                print("\n"+rojo_fondo+blanco+ "El Contacto  es:" +fin,azul, mostrar_codigo,fin)
            elif bucle == "4":
                print("\n"+azul+f"Ingrese el numero a actualizar: ", end=" "+fin)
                ruc1 = input()
                mostrar_codigo = contactos.get(ruc1, f'NO FIGURA EN TUS REGISTRO {ruc1}')
                for clave, valor in contactos.items():
                    if clave == ruc1:
                        print("\n"+amarillo+subrayado+"El contacto encontrado es:  ===>", end=" "+fin)
                        print(clave, contactos[clave])
                        nombre_empresa = input("\n"+violeta+"Ingresa el nuevo contacto: "+fin)
                        contactos[clave] = nombre_empresa
                        break
            elif bucle == "5":
                print("\n"+bordes+rojo+'Eliminar un contacto'+fin)
                codigos_final = contactos.keys()
                print("\n"+cyan+f"Ingrese el numero a eliminar:", end=" "+fin)
                codigo2 = input()
                for clave, valor in contactos.items():
                    if clave == codigo2:
                        print("\n"+rojo+"Eliminando al contacto ===>", end=" "+fin)
                        print(clave, contactos[clave])
                        break
                mostrar = contactos.get(codigo2, f'NO FIGURA EN TU CONTACTO {codigo2}')
                elimina_dato = contactos.pop(codigo2, f'NO EXISTE NUMERO{codigo2}')
            elif bucle == "0":
                break
            elif bucle != "1":
                print("\n"+bordes+rojo + 'Has ingresado opcion incorrecto' + fin)
                continue
#====================================================FIN DE LOS CONTACTOS===============================================