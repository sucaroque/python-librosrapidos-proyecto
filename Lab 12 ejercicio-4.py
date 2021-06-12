#Laboratorio 12 - Ejercicio 4
def lee_caracter(caracter):
  if (caracter=='a' or caracter=='e' or caracter=='i' or caracter=='o' or caracter=='u'):
    print(True)
  else:
    print(False)
  pass
dato = input('Ingrese un caracter:')
lee_caracter(dato)