print('\033[91m'+"SOLUCION PREGUNTA 7 - LABORATORIO 9"+'\033[0m')
listaNotas=[]
for x in range(5):
    valor=int(input("Ingrese nota\t:"))
    listaNotas.append(valor)
listaNotas.sort(reverse=True)
tuplaNotas = tuple (listaNotas)
listaFinal = list (tuplaNotas)
suma=0
reeemplazo=0
for i in listaFinal:
  suma +=i
promedio = round(suma/5)
for j in range(len(listaFinal)):
  if listaFinal[j] <= 10:
    listaFinal[j] = promedio
print('\033[1m'+"Promedio es\t:"+'\033[0m',promedio)
print("Las notas finales son: ",listaFinal)