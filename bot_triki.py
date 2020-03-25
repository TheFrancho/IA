def triki():

    matriz=[] #Definimos la matriz para relacionar las posiciones
    matriz=[['[0,0]','[0,1]','[0,2]'],['[1,0]','[1,1]','[1,2]'],['[2,0]','[2,1]','[2,2]']] #Llenamos los valores de ejemplo
    print("\nAsi se definira la matriz durante el juego:\n")
    for i in matriz: #Imprimimos la matriz de ejemplo
        print (i)
    print("\nAsi empezara el tablero:\n")
    matriz2=[['-' , '-', '-'], ['-', '-', '-'],['-', '-', '-']] #Definimos el tablero que se llenará
    for i in matriz2:#Imprimimos el tablero vacío
        print(i)
    y=0 #Definimos la variable y para el eje Y del tablero
    y=int(y) #La casteamos a int
    x=0 #Definimos la variable X para el eje X del tablero
    x=int(x) #La casteamos a int
    bandera=-1 #Variable para verificar si se está tratando de sobreescribir una casilla ya usada
    gameover=1 #Variable para definir que el juego terminó
    jugador=1 #Generamos un valor de jugador para determinar quien está jugando y cuantos turnos lleva el juego
    print("\nInicia el juego:")
    while(jugador<=10 and gameover!=0): #Mientras el juego lleve menos de 10 turnos y no se cumpla una win condition:
        if(((matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='X') #Todas las posibles win condition
        or (matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='X')
        or (matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='X')
        or (matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='X')
        or (matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='X')
        or (matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='X')
        or (matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='X'))
        or ((matriz2[0][0]=='O'and matriz2[1][1]=='O'and matriz2[2][2]=='O')
        or (matriz2[0][2]=='O'and matriz2[1][1]=='O'and matriz2[2][0]=='O')
        or (matriz2[0][0]=='O'and matriz2[1][0]=='O'and matriz2[2][0]=='O')
        or (matriz2[0][1]=='O'and matriz2[1][1]=='O'and matriz2[2][1]=='O')
        or (matriz2[0][2]=='O'and matriz2[1][2]=='O'and matriz2[2][2]=='O')
        or (matriz2[0][0]=='O'and matriz2[0][1]=='O'and matriz2[0][2]=='O')
        or (matriz2[2][0]=='O'and matriz2[2][1]=='O'and matriz2[2][2]=='O'))):
            print("juego terminado")
            gameover=0
        else:
            if (jugador%2==0): #Define que jugador está jugando, si es verdadero es porque es un turno par y juega el jugador 2
                print("\nJugador 2, juegue su turno numero "+ str(jugador)+ "\n")
            else: #Si es mentira es porque juega el jugador 1
                print("\nJugador 1, juegue su turno numero "+ str(jugador)+ "\n")
            while(bandera==-1): #Este while entero se va a encargar de evitar que se sobreescriban casillas en el tablero
                print("Elija la casilla a marcar (eje y)")
                x=int(input()) #Recibe el eje X
                while(x!=0 and x!=1 and x!=2): #Valida si el valor es posible en el tablero
                    print("Valor incorrecto, ingrese uno entre 0 y 2")
                    x=int(input())
                print("Elija la casilla a marcar (eje x)")
                y=int(input())
                while(y!=0 and y!=1 and y!=2):#Valida si el valor es posible en el tablero
                    print("Valor incorrecto, ingrese uno entre 0 y 2")
                    y=int(input())
                if(jugador%2==0): #Según el turno, coloca una X o una O
                    if (matriz2[x][y]!='X' and matriz2[x][y]!='O'): #Se verifica si alguno de los dos jugadores ha jugado ahi
                        matriz2[x][y]='X' #En este caso, el jugador 2 juega con la X
                        bandera=0 #El valor de la bandera pasa a 0, por lo que no vuelve a pedir la jugada
                    else:
                        print("jugada invalida")
                        bandera=-1 #La bandera es -1, por lo que la jugada fue invalida
                else:
                    if (matriz2[x][y]!='X' and matriz2[x][y]!='O'): #Se verifica si alguno de los dos jugadores ha jugado ahi
                        matriz2[x][y]='O' #En este caso, el jugador 2 juega con la X
                        bandera=0 #El valor de la bandera pasa a 0, por lo que no vuelve a pedir la jugada
                    else:
                        print("jugada invalida")
                        bandera=-1 #La bandera es -1, por lo que la jugada fue invalida
            jugador=jugador+1 #Incrementa el jugador actual
            bandera=-1 #Se vuelve a inicializar labandera en -1
            for i in matriz2: #Imprime el tablero actual
                print(i)
    #win_condition=
    #(matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='X') Diagonal de 135°
    #(matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='X') Diagonal de 225°
    #(matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='X') Primer vertical
    #(matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='X') Segundo vertical
    #(matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='X') Tercer vertical
    #(matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='X') Primer horizontal
    #(matriz2[1][0]=='X'and matriz2[1][1]=='X'and matriz2[1][2]=='X') Segundo horizontal
    #(matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='X') Tercer horizontal

def bot():

    matriz=[] #Definimos la matriz para relacionar las posiciones
    matriz=[['[0,0]','[0,1]','[0,2]'],['[1,0]','[1,1]','[1,2]'],['[2,0]','[2,1]','[2,2]']] #Llenamos los valores de ejemplo
    print("\nAsi se definira la matriz durante el juego:\n")
    for i in matriz: #Imprimimos la matriz de ejemplo
        print (i)
    print("\nAsi empezara el tablero:\n")
    matriz2=[['-' , '-', '-'], ['-', '-', '-'],['-', '-', '-']] #Definimos el tablero que se llenará
    for i in matriz2:#Imprimimos el tablero vacío
        print(i)
    y=0 #Definimos la variable y para el eje Y del tablero
    y=int(y) #La casteamos a int
    x=0 #Definimos la variable X para el eje X del tablero
    x=int(x) #La casteamos a int
    bandera=-1 #Variable para verificar si se está tratando de sobreescribir una casilla ya usada
    gameover=1 #Variable para definir que el juego terminó
    jugador=1 #Generamos un valor de jugador para determinar quien está jugando y cuantos turnos lleva el juego
    print("\nInicia el juego:")
    while(jugador<=5 and gameover!=0): #Mientras el juego lleve menos de 5 rondas y no se cumpla una win condition:
        if(((matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='X') #Todas las posibles win condition
        or (matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='X')
        or (matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='X')
        or (matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='X')
        or (matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='X')
        or (matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='X')
        or (matriz2[1][0]=='X'and matriz2[1][1]=='X'and matriz2[1][2]=='X')
        or (matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='X'))
        or ((matriz2[0][0]=='O'and matriz2[1][1]=='O'and matriz2[2][2]=='O')
        or (matriz2[0][2]=='O'and matriz2[1][1]=='O'and matriz2[2][0]=='O')
        or (matriz2[0][0]=='O'and matriz2[1][0]=='O'and matriz2[2][0]=='O')
        or (matriz2[0][1]=='O'and matriz2[1][1]=='O'and matriz2[2][1]=='O')
        or (matriz2[0][2]=='O'and matriz2[1][2]=='O'and matriz2[2][2]=='O')
        or (matriz2[0][0]=='O'and matriz2[0][1]=='O'and matriz2[0][2]=='O')
        or (matriz2[1][0]=='O'and matriz2[1][1]=='O'and matriz2[1][2]=='O')
        or (matriz2[2][0]=='O'and matriz2[2][1]=='O'and matriz2[2][2]=='O'))):
            print("juego terminado")
            gameover=0
        else:

            print("\nJugador 1: Haga su jugada")
            while(bandera==-1): #Este while entero se va a encargar de evitar que se sobreescriban casillas en el tablero
                print("Elija la casilla a marcar (eje y)")
                x=int(input()) #Recibe el eje X
                while(x!=0 and x!=1 and x!=2): #Valida si el valor es posible en el tablero
                    print("Valor incorrecto, ingrese uno entre 0 y 2")
                    x=int(input())
                print("Elija la casilla a marcar (eje x)")
                y=int(input())
                while(y!=0 and y!=1 and y!=2):#Valida si el valor es posible en el tablero
                    print("Valor incorrecto, ingrese uno entre 0 y 2")
                    y=int(input())
                if (matriz2[x][y]!='X' and matriz2[x][y]!='O'): #Se verifica si alguno de los dos jugadores ha jugado ahi
                    matriz2[x][y]='X' #En este caso, el jugador 2 juega con la X
                    bandera=0 #El valor de la bandera pasa a 0, por lo que no vuelve a pedir la jugada
                else:
                    print("jugada invalida")
                    bandera=-1 #La bandera es -1, por lo que la jugada fue invalida
            jugador=jugador+1 #Incrementa el jugador actual
            bandera=-1 #Se vuelve a inicializar labandera en -1
            for i in matriz2: #Imprime el tablero actual
                print(i)
            #A partir de aca juega el bot
            #El bot siempre va a verificar si puede ganar una partida, por lo que es su primera búsqueda:
            if (matriz2[0][0]=='O'and matriz2[1][1]=='O'and matriz2[2][2]=='-'): #Diagonal de 135°
                print("\njuega el bot:\n")
                matriz2[2][2]='O'
                for i in matriz2:
                    print (i)
            else:
                if (matriz2[0][0]=='O'and matriz2[1][1]=='-'and matriz2[2][2]=='O'):
                    print("\njuega el bot:\n")
                    matriz2[1][1]='O'
                    for i in matriz2:
                        print (i)
                else:
                    if (matriz2[0][0]=='-'and matriz2[1][1]=='O'and matriz2[2][2]=='O'):
                        print("\njuega el bot:\n")
                        matriz2[0][0]='O'
                        for i in matriz2:
                            print (i)
                    else:
                        if (matriz2[0][2]=='O'and matriz2[1][1]=='O'and matriz2[2][0]=='-'): #Diagonal de 225°
                            print("\njuega el bot:\n")
                            matriz2[2][0]='O'
                            for i in matriz2:
                                print (i)
                        else:
                            if (matriz2[0][2]=='O'and matriz2[1][1]=='-'and matriz2[2][0]=='O'):
                                print("\njuega el bot:\n")
                                matriz2[1][1]='O'
                                for i in matriz2:
                                    print (i)
                            else:
                                if (matriz2[0][2]=='-'and matriz2[1][1]=='O'and matriz2[2][0]=='O'):
                                    print("\njuega el bot:\n")
                                    matriz2[0][2]='O'
                                    for i in matriz2:
                                        print (i)
                                else:
                                    if (matriz2[0][0]=='O'and matriz2[1][0]=='O'and matriz2[2][0]=='-'): #Primer vertical
                                        print("\njuega el bot:\n")
                                        matriz2[2][0]='O'
                                        for i in matriz2:
                                            print (i)
                                    else:
                                        if (matriz2[0][0]=='O'and matriz2[1][0]=='-'and matriz2[2][0]=='O'):
                                            print("\njuega el bot:\n")
                                            matriz2[1][0]='O'
                                            for i in matriz2:
                                                print (i)
                                        else:
                                            if (matriz2[0][0]=='-'and matriz2[1][0]=='O'and matriz2[2][0]=='O'):
                                                print("\njuega el bot:\n")
                                                matriz2[0][0]='O'
                                                for i in matriz2:
                                                    print (i)
                                            else:
                                                if (matriz2[0][1]=='O'and matriz2[1][1]=='O'and matriz2[2][1]=='-'): #Segundo vertical
                                                    print("\njuega el bot:\n")
                                                    matriz2[2][1]='O'
                                                    for i in matriz2:
                                                        print (i)
                                                else:
                                                    if (matriz2[0][1]=='O'and matriz2[1][1]=='-'and matriz2[2][1]=='O'):
                                                        print("\njuega el bot:\n")
                                                        matriz2[1][1]='O'
                                                        for i in matriz2:
                                                            print (i)
                                                    else:
                                                        if (matriz2[0][1]=='-'and matriz2[1][1]=='O'and matriz2[2][1]=='O'):
                                                            print("\njuega el bot:\n")
                                                            matriz2[0][1]='O'
                                                            for i in matriz2:
                                                                print (i)
                                                        else:
                                                            if (matriz2[0][2]=='O'and matriz2[1][2]=='O'and matriz2[2][2]=='-'): #Tercera vertical
                                                                print("\njuega el bot:\n")
                                                                matriz2[2][2]='O'
                                                                for i in matriz2:
                                                                    print (i)
                                                            else:
                                                                if (matriz2[0][2]=='O'and matriz2[1][2]=='-'and matriz2[2][2]=='O'):
                                                                    print("\njuega el bot:\n")
                                                                    matriz2[1][2]='O'
                                                                    for i in matriz2:
                                                                        print (i)
                                                                else:
                                                                    if (matriz2[0][2]=='-'and matriz2[1][2]=='O'and matriz2[2][2]=='O'):
                                                                        print("\njuega el bot:\n")
                                                                        matriz2[0][2]='O'
                                                                        for i in matriz2:
                                                                            print (i)
                                                                    else:
                                                                        if (matriz2[0][0]=='O'and matriz2[0][1]=='O'and matriz2[0][2]=='-'): #Primer horizontal
                                                                            print("\njuega el bot:\n")
                                                                            matriz2[0][2]='O'
                                                                            for i in matriz2:
                                                                                print (i)
                                                                        else:
                                                                            if (matriz2[0][0]=='O'and matriz2[0][1]=='-'and matriz2[0][2]=='O'):
                                                                                print("\njuega el bot:\n")
                                                                                matriz2[0][1]='O'
                                                                                for i in matriz2:
                                                                                    print (i)
                                                                            else:
                                                                                if (matriz2[0][0]=='-'and matriz2[0][1]=='O'and matriz2[0][2]=='O'):
                                                                                    print("\njuega el bot:\n")
                                                                                    matriz2[0][0]='O'
                                                                                    for i in matriz2:
                                                                                        print (i)
                                                                                else:
                                                                                    if (matriz2[1][0]=='O'and matriz2[1][1]=='O'and matriz2[1][2]=='-'): #Segundo horizontal
                                                                                        print("\njuega el bot:\n")
                                                                                        matriz2[1][2]='O'
                                                                                        for i in matriz2:
                                                                                            print (i)
                                                                                    else:
                                                                                        if (matriz2[1][0]=='O'and matriz2[1][1]=='-'and matriz2[1][2]=='O'):
                                                                                            print("\njuega el bot:\n")
                                                                                            matriz2[1][1]='O'
                                                                                            for i in matriz2:
                                                                                                print (i)
                                                                                        else:
                                                                                            if (matriz2[1][0]=='-'and matriz2[1][1]=='O'and matriz2[1][2]=='O'):
                                                                                                print("\njuega el bot:\n")
                                                                                                matriz2[1][0]='O'
                                                                                                for i in matriz2:
                                                                                                    print (i)
                                                                                            else:
                                                                                                if (matriz2[2][0]=='O'and matriz2[2][1]=='O'and matriz2[2][2]=='-'): #Tercer horizontal
                                                                                                    print("\njuega el bot:\n")
                                                                                                    matriz2[2][2]='O'
                                                                                                    for i in matriz2:
                                                                                                        print (i)
                                                                                                else:
                                                                                                    if (matriz2[2][0]=='O'and matriz2[2][1]=='-'and matriz2[2][2]=='O'):
                                                                                                        print("\njuega el bot:\n")
                                                                                                        matriz2[2][1]='O'
                                                                                                        for i in matriz2:
                                                                                                            print (i)
                                                                                                    else:
                                                                                                        if (matriz2[2][0]=='-'and matriz2[2][1]=='O'and matriz2[2][2]=='O'):
                                                                                                            print("\njuega el bot:\n")
                                                                                                            matriz2[2][0]='O'
                                                                                                            for i in matriz2:
                                                                                                                print (i)
                                                                                                        else: #Si no encuentra condiciones para ganar, busca la manera de evitar perder
                                                                                                            if (matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='-'): #Diagonal de 135°
                                                                                                                print("\njuega el bot:\n")
                                                                                                                matriz2[2][2]='O'
                                                                                                                for i in matriz2:
                                                                                                                    print (i)
                                                                                                            else:
                                                                                                                if (matriz2[0][0]=='X'and matriz2[1][1]=='-'and matriz2[2][2]=='X'):
                                                                                                                    print("\njuega el bot:\n")
                                                                                                                    matriz2[1][1]='O'
                                                                                                                    for i in matriz2:
                                                                                                                        print (i)
                                                                                                                else:
                                                                                                                    if (matriz2[0][0]=='-'and matriz2[1][1]=='X'and matriz2[2][2]=='X'):
                                                                                                                        print("\njuega el bot:\n")
                                                                                                                        matriz2[0][0]='O'
                                                                                                                        for i in matriz2:
                                                                                                                            print (i)
                                                                                                                    else:
                                                                                                                        if (matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='-'): #Diagonal de 225°
                                                                                                                            print("\njuega el bot:\n")
                                                                                                                            matriz2[2][0]='O'
                                                                                                                            for i in matriz2:
                                                                                                                                print (i)
                                                                                                                        else:
                                                                                                                            if (matriz2[0][2]=='X'and matriz2[1][1]=='-'and matriz2[2][0]=='X'):
                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                matriz2[1][1]='O'
                                                                                                                                for i in matriz2:
                                                                                                                                    print (i)
                                                                                                                            else:
                                                                                                                                if (matriz2[0][2]=='-'and matriz2[1][1]=='X'and matriz2[2][0]=='X'):
                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                    matriz2[0][2]='O'
                                                                                                                                    for i in matriz2:
                                                                                                                                        print (i)
                                                                                                                                else:
                                                                                                                                    if (matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='-'): #Primer vertical
                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                        matriz2[2][0]='O'
                                                                                                                                        for i in matriz2:
                                                                                                                                            print (i)
                                                                                                                                    else:
                                                                                                                                        if (matriz2[0][0]=='X'and matriz2[1][0]=='-'and matriz2[2][0]=='X'):
                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                            matriz2[1][0]='O'
                                                                                                                                            for i in matriz2:
                                                                                                                                                print (i)
                                                                                                                                        else:
                                                                                                                                            if (matriz2[0][0]=='-'and matriz2[1][0]=='X'and matriz2[2][0]=='X'):
                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                matriz2[0][0]='O'
                                                                                                                                                for i in matriz2:
                                                                                                                                                    print (i)
                                                                                                                                            else:
                                                                                                                                                if (matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='-'): #Segundo vertical
                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                    matriz2[2][1]='O'
                                                                                                                                                    for i in matriz2:
                                                                                                                                                        print (i)
                                                                                                                                                else:
                                                                                                                                                    if (matriz2[0][1]=='X'and matriz2[1][1]=='-'and matriz2[2][1]=='X'):
                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                        matriz2[1][1]='O'
                                                                                                                                                        for i in matriz2:
                                                                                                                                                            print (i)
                                                                                                                                                    else:
                                                                                                                                                        if (matriz2[0][1]=='-'and matriz2[1][1]=='X'and matriz2[2][1]=='X'):
                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                            matriz2[0][1]='O'
                                                                                                                                                            for i in matriz2:
                                                                                                                                                                print (i)
                                                                                                                                                        else:
                                                                                                                                                            if (matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='-'): #Tercera vertical
                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                matriz2[2][2]='O'
                                                                                                                                                                for i in matriz2:
                                                                                                                                                                    print (i)
                                                                                                                                                            else:
                                                                                                                                                                if (matriz2[0][2]=='X'and matriz2[1][2]=='-'and matriz2[2][2]=='X'):
                                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                                    matriz2[1][2]='O'
                                                                                                                                                                    for i in matriz2:
                                                                                                                                                                        print (i)
                                                                                                                                                                else:
                                                                                                                                                                    if (matriz2[0][2]=='-'and matriz2[1][2]=='X'and matriz2[2][2]=='X'):
                                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                                        matriz2[0][2]='O'
                                                                                                                                                                        for i in matriz2:
                                                                                                                                                                            print (i)
                                                                                                                                                                    else:
                                                                                                                                                                        if (matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='-'): #Primer horizontal
                                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                                            matriz2[0][2]='O'
                                                                                                                                                                            for i in matriz2:
                                                                                                                                                                                print (i)
                                                                                                                                                                        else:
                                                                                                                                                                            if (matriz2[0][0]=='X'and matriz2[0][1]=='-'and matriz2[0][2]=='X'):
                                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                                matriz2[0][1]='O'
                                                                                                                                                                                for i in matriz2:
                                                                                                                                                                                    print (i)
                                                                                                                                                                            else:
                                                                                                                                                                                if (matriz2[0][0]=='-'and matriz2[0][1]=='X'and matriz2[0][2]=='X'):
                                                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                                                    matriz2[0][0]='O'
                                                                                                                                                                                    for i in matriz2:
                                                                                                                                                                                        print (i)
                                                                                                                                                                                else:
                                                                                                                                                                                    if (matriz2[1][0]=='X'and matriz2[1][1]=='X'and matriz2[1][2]=='-'): #Segundo horizontal
                                                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                                                        matriz2[1][2]='O'
                                                                                                                                                                                        for i in matriz2:
                                                                                                                                                                                            print (i)
                                                                                                                                                                                    else:
                                                                                                                                                                                        if (matriz2[1][0]=='X'and matriz2[1][1]=='-'and matriz2[1][2]=='X'):
                                                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                                                            matriz2[1][1]='O'
                                                                                                                                                                                            for i in matriz2:
                                                                                                                                                                                                print (i)
                                                                                                                                                                                        else:
                                                                                                                                                                                            if (matriz2[1][0]=='-'and matriz2[1][1]=='X'and matriz2[1][2]=='X'):
                                                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                                                matriz2[1][0]='O'
                                                                                                                                                                                                for i in matriz2:
                                                                                                                                                                                                    print (i)
                                                                                                                                                                                            else:
                                                                                                                                                                                                if (matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='-'): #Tercer horizontal
                                                                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                                                                    matriz2[2][2]='O'
                                                                                                                                                                                                    for i in matriz2:
                                                                                                                                                                                                        print (i)
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if (matriz2[2][0]=='X'and matriz2[2][1]=='-'and matriz2[2][2]=='X'):
                                                                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                                                                        matriz2[2][1]='O'
                                                                                                                                                                                                        for i in matriz2:
                                                                                                                                                                                                            print (i)
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if (matriz2[2][0]=='-'and matriz2[2][1]=='X'and matriz2[2][2]=='X'):
                                                                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                                                                            matriz2[2][0]='O'
                                                                                                                                                                                                            for i in matriz2:
                                                                                                                                                                                                                print (i)
                                                                                                                                                                                                        else: #Si no encuentra como ganar o evitar perder, señalara una casilla de alto valor
                                                                                                                                                                                                            if(matriz2[1][1]=='-' and matriz2[1][1]!='X' and matriz2[1][1]!='O'): #Primera prioridad: El centro
                                                                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                                                                matriz2[1][1]='O'
                                                                                                                                                                                                                for i in matriz2:
                                                                                                                                                                                                                    print(i)
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if(matriz2[0][0]=='-' and matriz2[0][0]!='X' and matriz2[0][0]!='O'): #Segunda prioridad: Esquinas
                                                                                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                                                                                    matriz2[0][0]='O'
                                                                                                                                                                                                                    for i in matriz2:
                                                                                                                                                                                                                        print(i)
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if(matriz2[0][2]=='-' and matriz2[0][2]!='X' and matriz2[0][2]!='O'):
                                                                                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                                                                                        matriz2[0][2]='O'
                                                                                                                                                                                                                        for i in matriz2:
                                                                                                                                                                                                                            print(i)
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if(matriz2[2][0]=='-' and matriz2[2][0]!='X' and matriz2[2][0]!='O'):
                                                                                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                                                                                            matriz2[2][0]='O'
                                                                                                                                                                                                                            for i in matriz2:
                                                                                                                                                                                                                                print(i)
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if(matriz2[2][2]=='-' and matriz2[2][2]!='X' and matriz2[2][2]!='O'):
                                                                                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                                                                                matriz2[2][2]='O'
                                                                                                                                                                                                                                for i in matriz2:
                                                                                                                                                                                                                                    print(i)
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                if(matriz2[0][1]=='-' and matriz2[0][1]!='X' and matriz2[0][1]!='O'): #Tercera proridad: Lados
                                                                                                                                                                                                                                    print("\njuega el bot:\n")
                                                                                                                                                                                                                                    matriz2[0][1]='O'
                                                                                                                                                                                                                                    for i in matriz2:
                                                                                                                                                                                                                                        print(i)
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                    if(matriz2[1][0]=='-' and matriz2[1][0]!='X' and matriz2[1][0]!='O'):
                                                                                                                                                                                                                                        print("\njuega el bot:\n")
                                                                                                                                                                                                                                        matriz2[1][0]='O'
                                                                                                                                                                                                                                        for i in matriz2:
                                                                                                                                                                                                                                            print(i)
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        if(matriz2[1][2]=='-' and matriz2[1][2]!='X' and matriz2[1][2]!='O'):
                                                                                                                                                                                                                                            print("\njuega el bot:\n")
                                                                                                                                                                                                                                            matriz2[1][2]='O'
                                                                                                                                                                                                                                            for i in matriz2:
                                                                                                                                                                                                                                                print(i)
                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            if(matriz2[2][1]=='-' and matriz2[2][1]!='X' and matriz2[2][1]!='O'):
                                                                                                                                                                                                                                                print("\njuega el bot:\n")
                                                                                                                                                                                                                                                matriz2[2][1]='O'
                                                                                                                                                                                                                                                for i in matriz2:
                                                                                                                                                                                                                                                    print(i)




def condiciones_bot(): #Esta función es no mas para visualizar mejor el programa

    matriz2=[['00' , '01', '02'], ['10', '11', '12'],['20', '21', '22']]
    prioridad0=[]
    prioridad0=matriz2[1][1]
    prioridad1=[]
    prioridad1=matriz2[0][0],matriz2[0][2],matriz2[2][0],matriz2[2][2]
    prioridad2=[]
    prioridad2=matriz2[0][1],matriz2[1][0],matriz2[1][2],matriz2[2][1]
    print(prioridad0, prioridad1, prioridad2)

    #win_condition=
    #(matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='X') Diagonal de 135°
    #(matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='X') Diagonal de 225°
    #(matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='X') Primer vertical
    #(matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='X') Segundo vertical
    #(matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='X') Tercer vertical
    #(matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='X') Primer horizontal
    #(matriz2[1][0]=='X'and matriz2[1][1]=='X'and matriz2[1][2]=='X') Segundo horizontal
    #(matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='X') Tercer horizontal


    #condiciones de riesgo
    #Primer paquete de 8
    #(matriz2[0][0]=='X'and matriz2[1][1]=='X'and matriz2[2][2]=='-') Variables de la diagonal de 135°
    #(matriz2[0][0]=='X'and matriz2[1][1]=='-'and matriz2[2][2]=='X') Variables de la diagonal de 135°
    #(matriz2[0][0]=='-'and matriz2[1][1]=='X'and matriz2[2][2]=='X') Variables de la diagonal de 135°

    #Segundo paquete de 8
    #(matriz2[0][2]=='X'and matriz2[1][1]=='X'and matriz2[2][0]=='-') Variables de la diagonal de 225°
    #(matriz2[0][2]=='X'and matriz2[1][1]=='-'and matriz2[2][0]=='X') Variables de la diagonal de 225°
    #(matriz2[0][2]=='-'and matriz2[1][1]=='X'and matriz2[2][0]=='X') Variables de la diagonal de 225°

    #Tercer paquete de 8
    #(matriz2[0][0]=='X'and matriz2[1][0]=='X'and matriz2[2][0]=='-') Variables de la primer vertical
    #(matriz2[0][0]=='X'and matriz2[1][0]=='-'and matriz2[2][0]=='X') Variables de la primer vertical
    #(matriz2[0][0]=='-'and matriz2[1][0]=='X'and matriz2[2][0]=='X') Variables de la primer vertical

    #Cuarto paquete de 8
    #(matriz2[0][1]=='X'and matriz2[1][1]=='X'and matriz2[2][1]=='-') Variables de la segundo vertical
    #(matriz2[0][1]=='X'and matriz2[1][1]=='-'and matriz2[2][1]=='X') Variables de la segundo vertical
    #(matriz2[0][1]=='-'and matriz2[1][1]=='X'and matriz2[2][1]=='X') Variables de la segundo vertical


    #(matriz2[0][2]=='X'and matriz2[1][2]=='X'and matriz2[2][2]=='-') Variables de la tercer vertical
    #(matriz2[0][2]=='X'and matriz2[1][2]=='-'and matriz2[2][2]=='X') Variables de la tercer vertical
    #(matriz2[0][2]=='-'and matriz2[1][2]=='X'and matriz2[2][2]=='X') Variables de la tercer vertical


    #(matriz2[0][0]=='X'and matriz2[0][1]=='X'and matriz2[0][2]=='-') Variables del primer horizontal
    #(matriz2[0][0]=='X'and matriz2[0][1]=='-'and matriz2[0][2]=='X') Variables del primer horizontal
    #(matriz2[0][0]=='-'and matriz2[0][1]=='X'and matriz2[0][2]=='X') Variables del primer horizontal


    #(matriz2[1][0]=='X'and matriz2[1][1]=='X'and matriz2[1][2]=='-') Variables del segundo horizontal
    #(matriz2[1][0]=='X'and matriz2[1][1]=='-'and matriz2[1][2]=='X') Variables del segundo horizontal
    #(matriz2[1][0]=='-'and matriz2[1][1]=='X'and matriz2[1][2]=='X') Variables del segundo horizontal

    #(matriz2[2][0]=='X'and matriz2[2][1]=='X'and matriz2[2][2]=='-') Variables del tercer horizontal
    #(matriz2[2][0]=='X'and matriz2[2][1]=='-'and matriz2[2][2]=='X') Variables del tercer horizontal
    #(matriz2[2][0]=='-'and matriz2[2][1]=='X'and matriz2[2][2]=='X') Variables del tercer horizontal

if __name__ == '__main__':
    #triki()
    bot()
