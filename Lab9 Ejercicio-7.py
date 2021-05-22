print('\033[91m'+"SOLUCION PREGUNTA 7 - LABORATORIO 9"+'\033[0m')
listaNotas=[]
for x in range(10):
    valor=int(input(f"Ingrese nota {x+1}\t:"))
    listaNotas.append(valor)
listaNotas.sort(reverse=True)
tuplaNotas = tuple (listaNotas)
listaFinal = list (tuplaNotas)
suma=0
reeemplazo=0
for i in listaFinal:
  suma +=i
promedio = round(suma/10)
for j in range(len(listaFinal)):
  if listaFinal[j] <= 10:
    listaFinal[j] = promedio
print('\033[1m'+"Promedio de las 10 notas es:"+'\033[0m',promedio)
print("Las notas finales son: ",listaFinal)