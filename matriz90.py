#Deyka Jordan Aula 2096
mat=[]

Dim = int(input("Ingrese la dimensión de la matriz: "))
for d in range(0,Dim) :
    mat.append(input("Ingrese los valores de las filas separados por espacios: ").split())

print("Matriz Original")

# Funcion que permite imprimir la matrix
def imprimirMatriz(mat):
	
	for d in range(0,Dim):
		
		for j in range(0,Dim):
			
			print (mat[d][j], end = ' ')
		print ("")
	
imprimirMatriz(mat)

# Funcion que permite la rotación de la matriz
def rotarMatriz(mat):

	for d in range(0,int(Dim/2)):

		for j in range(d, Dim-d-1):
			
			temp = mat[d][j]
			
			mat[d][j] = mat[j][Dim-1-d]

			mat[j][Dim-1-d] = mat[Dim-1-d][Dim-1-j]

			mat[Dim-1-d][Dim-1-j] = mat[Dim-1-j][d]

			mat[Dim-1-j][d] = temp

rotarMatriz(mat)

print("Matriz Rotada")

imprimirMatriz(mat)

