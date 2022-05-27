#Fernando Gómez Martínez    A01641228
#Carlos José Cortez Loya    A01566136
#Josué Alvarado Morales     A01634775

#RETO: JUEGO COGNITIVO: SUDOKU


#Inicializar variables
import random
Sudoku = []
clave = []
user = []

def Create(matriz_1, matriz_2):     #Crear matriz resuelta y matriz de usuario
    #Llenamos la lista con 0's
    for i in range (9):
        matriz_1.append([0]*9)
        matriz_2.append([0]*9)
    

    #introduciremos a la matriz 17 valores aleatorios en coordenadas aleatorias de la matriz
    #estos son los valores necesarios para que nuestro sudoku tenga unicamente una respuesta
    for i in range (17):
        valor_filas = random.randrange(9)
        valor_col = random.randrange(9)
        valor_num = random.randrange(1,10)
        
        while (not Comprobar(matriz_1, valor_filas, valor_col, valor_num) and matriz_1[valor_filas][valor_col] != 0) or (matriz_1[valor_filas][valor_col] == 0 and not Comprobar(matriz_1, valor_filas, valor_col, valor_num)) or (matriz_1[valor_filas][valor_col] != 0):
            valor_filas = random.randrange(9)
            valor_col = random.randrange(9)
            valor_num = random.randrange(1,10)
        #Insertamos los valores en la matriz con respuestas, y en la matriz con la que va a interacruar el usuario
        matriz_1[valor_filas][valor_col] = valor_num
        matriz_2[valor_filas][valor_col] = valor_num

def Show_Grid(matriz):
    #Definimos el formato de la tabla que se verá en la consola
    base = "|-----------------------------------|"
    print(base)
    for i in range (9):
        for j in range (9):
            if (i == 3 or i == 6) and j == 0:
                print (base)
            if j % 3 == 0:
                print("| ", end=" ")
            print (str(matriz[i][j]), end="  ")
            if j == 8:
                print ("|")
    print (base)

def Comprobar(lista, fila, col, val):
    check = True
    #Comprobamos que no este en la misma fila o columna
    for i in range (9):
        if lista [i][col] == val and lista[0] != i:
            return False

    for j in range (9):
        if lista[fila][j] == val and lista[1] != j:
            return False

    #Definir valores para determinar cuadros
    cuadro_x = fila // 3
    cuadro_y = col // 3
    
    #detectamos la posicion minima del cuadro en x
    if cuadro_x == 0:
        val_min_x = 0
    elif cuadro_x == 1:
        val_min_x = 3
    else:
        val_min_x = 6

    #detectamos la posicion minima del cuadro en y
    if cuadro_y == 0:
        val_min_y = 0
    elif cuadro_y == 1:
        val_min_y = 3
    else:
        val_min_y = 6
    #Recorremos y comparamos cada valor de nuestro cuadro
    for i in range (3):
        for j in range (3):
            if lista[val_min_x + i][val_min_y + j] == val:
                return False            
    return check

def Solve(lista_sud):
    done = Casilla_vacia(user)
    while done:
        #Pedir al usuario la coordenada y el valor deseados
        y = int(input("\nCoordenada en x (columna): "))
        x = int(input("Coordenada en y (fila): "))
        num = int(input("Valor a colocar (entre 1 y 9): "))

        #Error tipo 1: valores fuera de rango
        while num>9 or num<1 or y>9 or y<1 or x>9 or x<1:
            print("\nError: Valor(es) Inválido(s). Intentelo de nuevo\n")
            y = int(input("\nCoordenada en x (columna del 1 al 9): "))
            x = int(input("Coordenada en y (fila del 1 al 9): "))
            num = int(input("Valor a colocar (entre 1 y 9): "))

        #Error tipo 2: coordenada es un valor ya establecido
        while  lista_sud[x-1][y-1] != 0:
            print("\nError: la coordenada seleccionada es un valor no modificable. Inténtelo de nuevo\n")
            y = int(input("Coordenada en x (columna del 1 al 9): "))
            x = int(input("Coordenada en y (fila del 1 al 9): "))
            num = int(input("Valor a colocar (entre 1 y 9): "))

        lista_sud[x-1][y-1] = num
        Show_Grid(lista_sud)
        done = Casilla_vacia(lista_sud)

    #Comparacion de matrices
    if user == clave:
        print ("GANASTE :)")
    else:
        print ("\nPERDISTE. Tienes errores :(")
        print ("La respuesta correcta es: ")
        Show_Grid(clave)

def Answer(matriz):     #Genera la lista llena de las respuestas correctas BACKTRACKING
    #Revisa que aun haya casillas sin respuesta
    casilla = Casilla_vacia(matriz)
    if not casilla:
        #Si todas las casillas estan completas, se sale de la función
        return True
    else:
        fila, col = casilla

    #Comprobar las combimnaciones correctas por medio de backtracking
    for i in range (1,10):
        if Comprobar(matriz, fila, col, i):
            matriz[fila][col] = i
            if Answer(matriz):
                #Vamos por buen camino
                return True
            #Nuestro valor era incorrecto, y se resetea a 0
            matriz[fila][col] = 0
    return False

    

def Casilla_vacia(grid):
    #Detectamos la primera casilla vacía en nuestra matriz
    for i in range (9):
        for j in range (9):
            if grid[i][j] == 0:
                #Se detiene el encontrar el primer espacio vacio
                return (i, j)       #filas, columnas

    #Si no hay espacio vacío regresa un valor tipo None
    return None
    
def Instrucciones():
    #Instrucciones y reglas del juego en la consola
    print("\n \nBIENVENID@ AL JUEGO DEL SUDOKU")  
    print("En este juego, el objetivo es colocar numeros del 1 al 9 en cada cuadro, pero hay una regla:")
    print("NO SE PUEDE REPETIR EL MISMO NUMERO EN LA FILA, COLUMNA, NI RECUADRO EN EL QUE SE POSICIONE EL NÚMERO")
    print("\nPara insertar valores, se le pedirá que ingrese la fila y la columna en donde quiere poner el valor, seguido del numero a poner en la coordenada")
    print("\nOJO: SOLAMENTE PUEDE MODIFICAR LAS POSICIONES EN LAS QUE APAREZCA UN NÚMERO '0'")
    print("¡Buena Suerte! :)\n")

def matriz_usuario(respuesta):
    # hacer lista de 9x9
    for i in range (9):
        user.append([0]*9)

    #Se llena la matriz que el usuario va a modificar basada en la matriz respondida
    for i in range (31): #Numero de casillas que se van a mostrar (entre menos numeros, mayor la dificultad)
        fila = random.randrange(9)
        col = random.randrange(9)
        while user[fila][col] != 0:
            fila = random.randrange(9)
            col = random.randrange(9)

        user[fila][col] = respuesta[fila][col]

def main():
    #Función principal
    Instrucciones()    
    Create(Sudoku,clave)
    Answer(clave)
    matriz_usuario(clave)
    print("\n")
    Show_Grid(user)
    print("\n")
    print("\n")
    Solve(user)
main()
