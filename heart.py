print("CON MUCHO CARIÑO PARA SUSSAN")
for fila in range(6):
	for columna in range(7):
		if (fila==0 and columna%3!=0) or (fila==1 and columna%3==0) or (fila-columna==2) or (fila+columna==8):
			print("*",end="")
		else:
			print(end=" ")
	print()
