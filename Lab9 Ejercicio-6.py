print("SOLUCION PREGUNTA 6 - LABORATORIOS 9")
notas = (8,14,19,12,10,13,10,12,11,12,13,12,17,19,12,14,11,8,12,16)
desaprobados=0
aprobados=0
for i in notas:
  if i<13:
    desaprobados +=1
  elif i>=13:
    aprobados +=1
print("Total de estudiantes desaprobados\t:",desaprobados)
print("Total de estudiantes aprobados\t:",aprobados)