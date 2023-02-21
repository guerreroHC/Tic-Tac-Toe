import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayerSimbol = "X"
winner = None
gamerunning = True

# printing the game board | Imprimiendo la mesa de juego
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input | tomar la entrada de datos del usuario
def playerInput (board):
    numberInput = int(input("Enter a number 1-9: "))
    print("")
    # Here we are gonna validate if the location the user wants to use is
    # avalaible | Aqui vamos a verificar si la ubicacion que el usuario desea
    # ingresar esta libre. 
    if numberInput >= 1 and numberInput <=9 and board[numberInput-1] == "-": 
        board[numberInput-1] = currentPlayerSimbol
    else: 
        numb = numberInput
        print(f"The spot number {numb} is already taken...")
        print("Enter a different number please")
        print("")
        playerInput(board)
    

# Check for win or tie | Verificar si gana o empata

# First, we check if there is a win in the horizontale lines | Primero 
# verificamos si hay ganador en las lineas horizontales
def checkHorizontale(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# We check if there is a win in the vertical lines |
# verificamos si hay ganador en las lineas verticales
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# We check if there is a win in the diagonal lines |
# verificamos si hay ganador en las lineas diagonales
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# We check if there is a tie |
# verificamos si hay empate
def checkTie(board):
    global gamerunning
    if "-" not in board:
        # If there is no "-" in the board, that means that there is a tie
        # because you will never use every single space if you win. |
        # Si no hay "-" en la mesa de juego, significa que hay un empate
        # porque nunca vas a usar todos los espacios si ganas. 
        printBoard(board)
        print("It is a tie...")
        gamerunning = False
        return True

# We check if there is a win |
# verificamos si hay ganador
def checkWin(board):
    global gamerunning
    if checkDiagonal(board) or checkHorizontale(board) or checkVertical(board):
        printBoard(board)
        print("")
        print(f"The winner is {winner}")
        print("")
        gamerunning = False
        return True
        
# Switch the player | Cambiar el jugador
def switchPlayer():
    global currentPlayerSimbol
    if currentPlayerSimbol == "X":
        currentPlayerSimbol = "O"
    else:
        currentPlayerSimbol = "X"

# Computer movement | Movimientos de la computadora
def computer(board):
    while currentPlayerSimbol == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



while gamerunning:    
    printBoard(board)
    playerInput(board)
    if checkWin(board):
        break
    if checkTie(board):
        break
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)