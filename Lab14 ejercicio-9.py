from datetime import datetime
now = datetime.now()
archivo = open('nombres.txt','wt')
nro = 1
promedio=0
archivo.write('Registro de Notas\n')
archivo.write('======== == =====\n')
while True:
	nombre = input('Ingrese nombre de contacto : ')
	if nombre== '':
		break
	curso = input('Ingrese el curso :')
	nota1 = int(input('Ingrese nota 1 :'))
	nota2 = int(input('Ingrese nota 2 :'))
	not1=str(nota1)
	not2=str(nota2)
	promedio=(nota1+nota2)/2
	final=str(promedio)
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	if promedio>=13:
		condicion="Aprobado"
	else:
		condicion="Desaprobado"
	archivo.write(nombre+': '+curso+': '+not1+': '+not2+': '+'prom:'+final+': '+condicion+': '+date_time+'\n')
	nro += 1
archivo.close()