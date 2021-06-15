# on line number 481 reduce the max value of depth if it is taking a lot of time
# at last there is code for 2d tic tac toe

board = {1: ' ', 2: ' ', 3: ' ',    10: ' ', 11: ' ', 12: ' ',    19: ' ', 20: ' ', 21: ' ',
         4: ' ', 5: ' ', 6: ' ',    13: ' ', 14: ' ', 15: ' ',    22: ' ', 23: ' ', 24: ' ',
         7: ' ', 8: ' ', 9: ' ',    16: ' ', 17: ' ', 18: ' ',    25: ' ', 26: ' ', 27: ' '}
         
def showBoard(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + '  ' +board[10] + ' | ' + board[11] + ' | ' + board[12] + '  '+ board[19] + ' | ' + board[20] + ' | ' + board[21] )
    print('--+---+--  --+---+--  --+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + '  ' +board[13] + ' | ' + board[14] + ' | ' + board[15] + '  '+ board[22] + ' | ' + board[23] + ' | ' + board[24])
    print('--+---+--  --+---+--  --+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + '  ' +board[16] + ' | ' + board[17] + ' | ' + board[18] + '  '+ board[25] + ' | ' + board[26] + ' | ' + board[27])


showBoard(board) 

def isEmptySpot(position):
    if (board[position] == ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
        
    return True

def checkWIN():
    #rows
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        return True
    # layer 2    
    elif (board[10] == board[11] and board[11] == board[12] and board[10] != ' '):
        return True
    elif (board[13] == board[14] and board[14] == board[15] and board[13] != ' '):
        return True
    elif (board[16] == board[17] and board[17] == board[18] and board[16] != ' '):
        return True
    #layer 3
    elif (board[19] == board[20] and board[20] == board[21] and board[21] != ' '):
        return True
    elif (board[22] == board[23] and board[23] == board[24] and board[24] != ' '):
        return True
    elif (board[25] == board[26] and board[26] == board[27] and board[27] != ' '):
        return True
    # columns
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        return True
    #layer 2
    elif (board[10] == board[13] and board[13] == board[16] and board[16] != ' '):
        return True
    elif (board[11] == board[14] and board[14] == board[17] and board[17] != ' '):
        return True
    elif (board[12] == board[15] and board[15] == board[18] and board[18] != ' '):
        return True
    #layer 3
    elif (board[19] == board[22] and board[22] == board[25] and board[25] != ' '):
        return True
    elif (board[20] == board[23] and board[23] == board[26] and board[26] != ' '):
        return True
    elif (board[21] == board[24] and board[24] == board[27] and board[27] != ' '):
        return True
 
    # verticals
    elif (board[1] == board[10] and board[10] == board[19] and board[1] != ' '):
        return True
    elif (board[2] == board[11] and board[11] == board[20] and board[2] != ' '):
        return True
    elif (board[3] == board[12] and board[12] == board[21] and board[3] != ' '):
        return True
    elif (board[4] == board[13] and board[13] == board[22] and board[4] != ' '):
        return True
    elif (board[5] == board[14] and board[14] == board[23] and board[5] != ' '):
        return True
    elif (board[6] == board[15] and board[15] == board[24] and board[6] != ' '):
        return True
    elif (board[7] == board[16] and board[16] == board[25] and board[7] != ' '):
        return True
    elif (board[8] == board[17] and board[17] == board[26] and board[8] != ' '):
        return True
    elif (board[9] == board[18] and board[18] == board[27] and board[9] != ' '):
        return True

    # diagonal 2d x-y plane
    elif (board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] != ' '):
        return True
    elif (board[10] == board[14] and board[14] == board[18] and board[10] != ' '):
        return True
    elif (board[12] == board[14] and board[14] == board[16] and board[16] != ' '):
        return True
    elif (board[19] == board[23] and board[23] == board[27] and board[27] != ' '):
        return True
    elif (board[21] == board[23] and board[23] == board[25] and board[25] != ' '):
        return True
    
    #diagonal 2d yz plane --> 19 11 3; 21 11 1;
    #                         22 14 6; 24 14 4
    #                         25 17 9; 27 17 7
    elif (board[19] == board[11] and board[11] == board[3] and board[3] != ' '):
        return True
    elif (board[21] == board[11] and board[11] == board[6] and board[6] != ' '):
        return True

    elif (board[22] == board[14] and board[14] == board[6] and board[14] != ' '):
        return True
    elif (board[24] == board[14] and board[14] == board[4] and board[14] != ' '):
        return True

    elif (board[25] == board[17] and board[17] == board[9] and board[17] != ' '):
        return True
    elif (board[27] == board[17] and board[17] == board[7] and board[17] != ' '):
        return True

    # diagonal 2d xz plane --> 1 13 25; 7 13 19; 2 14 26; 8 14 20; 3 15 27; 9 15 21
    elif (board[1] == board[13] and board[13] == board[25] and board[25] != ' '):
        return True
    elif (board[7] == board[13] and board[13] == board[19] and board[19] != ' '):
        return True

    elif (board[2] == board[14] and board[14] == board[26] and board[26] != ' '):
        return True
    elif (board[8] == board[14] and board[14] == board[20] and board[20] != ' '):
        return True
    
    elif (board[3] == board[15] and board[15] == board[27] and board[27] != ' '):
        return True
    elif (board[9] == board[15] and board[15] == board[21] and board[21] != ' '):
        return True

    # diagonal 3d --> 1 14 27; 3 14 25; 9 14 19; 7 14 21
    elif (board[1] == board[14] and board[14] == board[27] and board[14] != ' '):
        return True
    elif (board[3] == board[14] and board[14] == board[25] and board[14] != ' '):
        return True
    elif (board[9] == board[14] and board[14] == board[19] and board[14] != ' '):
        return True
    elif (board[7] == board[14] and board[14] == board[21] and board[14] != ' '):
        return True


    else:
        return False
        
def whoWIN(mark):
    #rows
    if (board[1] == board[2] and board[2] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] == mark):
        return True
    # layer 2    
    elif (board[10] == board[11] and board[11] == board[12] and board[10] == mark):
        return True
    elif (board[13] == board[14] and board[14] == board[15] and board[13] == mark):
        return True
    elif (board[16] == board[17] and board[17] == board[18] and board[16] == mark):
        return True
    #layer 3
    elif (board[19] == board[20] and board[20] == board[21] and board[21] == mark):
        return True
    elif (board[22] == board[23] and board[23] == board[24] and board[24] == mark):
        return True
    elif (board[25] == board[26] and board[26] == board[27] and board[27] == mark):
        return True
    # columns
    elif (board[1] == board[4] and board[4] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] == mark):
        return True
    #layer 2
    elif (board[10] == board[13] and board[13] == board[16] and board[16] == mark):
        return True
    elif (board[11] == board[14] and board[14] == board[17] and board[17] == mark):
        return True
    elif (board[12] == board[15] and board[15] == board[18] and board[18] == mark):
        return True
    #layer 3
    elif (board[19] == board[22] and board[22] == board[25] and board[25] == mark):
        return True
    elif (board[20] == board[23] and board[23] == board[26] and board[26] == mark):
        return True
    elif (board[21] == board[24] and board[24] == board[27] and board[27] == mark):
        return True

    # verticals
    elif (board[1] == board[10] and board[10] == board[19] and board[1] == mark):
        return True
    elif (board[2] == board[11] and board[11] == board[20] and board[2] == mark):
        return True
    elif (board[3] == board[12] and board[12] == board[21] and board[3] == mark):
        return True
    elif (board[4] == board[13] and board[13] == board[22] and board[4] == mark):
        return True
    elif (board[5] == board[14] and board[14] == board[23] and board[5] == mark):
        return True
    elif (board[6] == board[15] and board[15] == board[24] and board[6] == mark):
        return True
    elif (board[7] == board[16] and board[16] == board[25] and board[7] == mark):
        return True
    elif (board[8] == board[17] and board[17] == board[26] and board[8] == mark):
        return True
    elif (board[9] == board[18] and board[18] == board[27] and board[9] == mark):
        return True

    # diagonal 2d x-y plane
    elif (board[1] == board[5] and board[5] == board[9] and board[1] == mark):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] == mark):
        return True
    elif (board[10] == board[14] and board[14] == board[18] and board[10] == mark):
        return True
    elif (board[12] == board[14] and board[14] == board[16] and board[16] == mark):
        return True
    elif (board[19] == board[23] and board[23] == board[27] and board[27] == mark):
        return True
    elif (board[21] == board[23] and board[23] == board[25] and board[25] == mark):
        return True
    
    #diagonal 2d yz plane --> 19 11 3; 21 11 1;
    #                         22 14 6; 24 14 4
    #                         25 17 9; 27 17 7
    elif (board[19] == board[11] and board[11] == board[3] and board[3] == mark):
        return True
    elif (board[21] == board[11] and board[11] == board[6] and board[6] == mark):
        return True

    elif (board[22] == board[14] and board[14] == board[6] and board[14] == mark):
        return True
    elif (board[24] == board[14] and board[14] == board[4] and board[14] == mark):
        return True

    elif (board[25] == board[17] and board[17] == board[9] and board[17] == mark):
        return True
    elif (board[27] == board[17] and board[17] == board[7] and board[17] == mark):
        return True

    # diagonal 2d xz plane --> 1 13 25; 7 13 19; 2 14 26; 8 14 20; 3 15 27; 9 15 21
    elif (board[1] == board[13] and board[13] == board[25] and board[25] == mark):
        return True
    elif (board[7] == board[13] and board[13] == board[19] and board[19] == mark):
        return True

    elif (board[2] == board[14] and board[14] == board[26] and board[26] == mark):
        return True
    elif (board[8] == board[14] and board[14] == board[20] and board[20] == mark):
        return True
    
    elif (board[3] == board[15] and board[15] == board[27] and board[27] == mark):
        return True
    elif (board[9] == board[15] and board[15] == board[21] and board[21] == mark):
        return True

    # diagonal 3d --> 1 14 27; 3 14 25; 9 14 19; 7 14 21
    elif (board[1] == board[14] and board[14] == board[27] and board[14] == mark):
        return True
    elif (board[3] == board[14] and board[14] == board[25] and board[14] == mark):
        return True
    elif (board[9] == board[14] and board[14] == board[19] and board[14] == mark):
        return True
    elif (board[7] == board[14] and board[14] == board[21] and board[14] == mark):
        return True
    
    else:
        return False

def markMove (mark,position):

    if isEmptySpot(position):
        board[position] = mark
        showBoard(board)
        if(checkDraw()):
            print("Draw")
            exit()
        
        if checkWIN() :
            if mark == 'X':
                print("Better luck next time")
                exit()
            else:
                print("You win")
                exit()
        return
    else:
        print("Not a possible move")
        position = int(input("Enter another position"))
        markMove(mark,position)
        return

player = 'O'
bot = 'X'

def pseudocheckWIN (board, mark):
    
    winCounter = 0
    #rows
    if ((board[1] == mark or board[1] == ' ') and (board[2] == mark or board[2] == ' ') and (board[3] == mark or board[3] == ' ')):
        winCounter += 1 
    if ((board[4] == mark or board[4] == ' ') and (board[5] == mark or board[5] == ' ') and (board[6] == mark or board[6] == ' ')):
        winCounter += 1
    if ((board[7] == mark or board[7] == ' ') and (board[8] == mark or board[8] == ' ') and (board[9] == mark or board[9] == ' ')):
        winCounter += 1
    #board 2
    if ((board[10] == mark or board[10] == ' ') and (board[11] == mark or board[11] == ' ') and (board[12] == mark or board[12] == ' ')):
        winCounter += 1
    if ((board[13] == mark or board[13] == ' ') and (board[14] == mark or board[14] == ' ') and (board[15] == mark or board[15] == ' ')):
        winCounter += 1
    if ((board[16] == mark or board[16] == ' ') and (board[17] == mark or board[17] == ' ') and (board[18] == mark or board[18] == ' ')):
        winCounter += 1
    #board3
    if ((board[19] == mark or board[19] == ' ') and (board[20] == mark or board[20] == ' ') and (board[21] == mark or board[21] == ' ')):
        winCounter += 1
    if ((board[22] == mark or board[22] == ' ') and (board[23] == mark or board[23] == ' ') and (board[24] == mark or board[24] == ' ')):
        winCounter += 1
    if ((board[25] == mark or board[25] == ' ') and (board[26] == mark or board[26] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1
        
        
    #columns    
    if ((board[1] == mark or board[1] == ' ') and (board[4] == mark or board[4] == ' ') and (board[7] == mark or board[7] == ' ')):
        winCounter += 1
    if ((board[2] == mark or board[2] == ' ') and (board[5] == mark or board[5] == ' ') and (board[8] == mark or board[8] == ' ')):
        winCounter += 1
    if ((board[3] == mark or board[3] == ' ') and (board[6] == mark or board[6] == ' ') and (board[9] == mark or board[9] == ' ')):
        winCounter += 1
    #board 2
    if ((board[10] == mark or board[10] == ' ') and (board[13] == mark or board[13] == ' ') and (board[16] == mark or board[16] == ' ')):
        winCounter += 1
    if ((board[11] == mark or board[11] == ' ') and (board[14] == mark or board[14] == ' ') and (board[17] == mark or board[17] == ' ')):
        winCounter += 1
    if ((board[12] == mark or board[12] == ' ') and (board[15] == mark or board[15] == ' ') and (board[18] == mark or board[18] == ' ')):
        winCounter += 1
    #board 3
    if ((board[19] == mark or board[19] == ' ') and (board[22] == mark or board[22] == ' ') and (board[25] == mark or board[25] == ' ')):
        winCounter += 1
    if ((board[20] == mark or board[20] == ' ') and (board[23] == mark or board[23] == ' ') and (board[26] == mark or board[26] == ' ')):
        winCounter += 1
    if ((board[21] == mark or board[21] == ' ') and (board[24] == mark or board[24] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1
        
    
    #verticals
    if ((board[1] == mark or board[1] == ' ') and (board[10] == mark or board[10] == ' ') and (board[19] == mark or board[19] == ' ')):
        winCounter += 1
    if ((board[2] == mark or board[2] == ' ') and (board[11] == mark or board[11] == ' ') and (board[20] == mark or board[20] == ' ')):
        winCounter += 1
    if ((board[3] == mark or board[3] == ' ') and (board[12] == mark or board[12] == ' ') and (board[21] == mark or board[21] == ' ')):
        winCounter += 1
    if ((board[4] == mark or board[4] == ' ') and (board[13] == mark or board[13] == ' ') and (board[22] == mark or board[22] == ' ')):
        winCounter += 1
    if ((board[5] == mark or board[5] == ' ') and (board[14] == mark or board[14] == ' ') and (board[23] == mark or board[23] == ' ')):
        winCounter += 1
    if ((board[6] == mark or board[6] == ' ') and (board[15] == mark or board[15] == ' ') and (board[24] == mark or board[24] == ' ')):
        winCounter += 1
    if ((board[7] == mark or board[7] == ' ') and (board[16] == mark or board[16] == ' ') and (board[25] == mark or board[25] == ' ')):
        winCounter += 1
    if ((board[8] == mark or board[8] == ' ') and (board[17] == mark or board[17] == ' ') and (board[26] == mark or board[26] == ' ')):
        winCounter += 1
    if ((board[9] == mark or board[9] == ' ') and (board[18] == mark or board[18] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1

    #diagonal x-y 
    if ((board[1] == mark or board[1] == ' ') and (board[5] == mark or board[5] == ' ') and (board[9] == mark or board[9] == ' ')):
        winCounter += 1
    if ((board[3] == mark or board[3] == ' ') and (board[5] == mark or board[5] == ' ') and (board[7] == mark or board[9] == ' ')):
        winCounter += 1
        
    if ((board[10] == mark or board[10] == ' ') and (board[14] == mark or board[14] == ' ') and (board[18] == mark or board[18] == ' ')):
        winCounter += 1
    if ((board[12] == mark or board[12] == ' ') and (board[14] == mark or board[14] == ' ') and (board[16] == mark or board[16] == ' ')):
        winCounter += 1
    
    if ((board[19] == mark or board[19] == ' ') and (board[23] == mark or board[23] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1
    if ((board[21] == mark or board[21] == ' ') and (board[23] == mark or board[23] == ' ') and (board[25] == mark or board[25] == ' ')):
        winCounter += 1
    
    
    #diagonal 2d yz plane --> 19 11 3; 21 11 1;
    #                         22 14 6; 24 14 4
    #                         25 17 9; 27 17 7
    if ((board[19] == mark or board[19] == ' ') and (board[11] == mark or board[11] == ' ') and (board[3] == mark or board[3] == ' ')):
        winCounter += 1
    if ((board[22] == mark or board[22] == ' ') and (board[14] == mark or board[14] == ' ') and (board[6] == mark or board[6] == ' ')):
        winCounter += 1
    if ((board[25] == mark or board[25] == ' ') and (board[17] == mark or board[17] == ' ') and (board[9] == mark or board[9] == ' ')):
        winCounter += 1
    if ((board[21] == mark or board[21] == ' ') and (board[11] == mark or board[11] == ' ') and (board[1] == mark or board[1] == ' ')):
        winCounter += 1
    if ((board[24] == mark or board[24] == ' ') and (board[14] == mark or board[14] == ' ') and (board[4] == mark or board[4] == ' ')):
        winCounter += 1
    if ((board[27] == mark or board[27] == ' ') and (board[17] == mark or board[17] == ' ') and (board[7] == mark or board[7] == ' ')):
        winCounter += 1
        
        
    # diagonal 2d xz plane --> 1 13 25; 7 13 19; 2 14 26; 8 14 20; 3 15 27; 9 15 21
    if ((board[1] == mark or board[1] == ' ') and (board[13] == mark or board[13] == ' ') and (board[25] == mark or board[25] == ' ')):
        winCounter += 1
    if ((board[7] == mark or board[7] == ' ') and (board[13] == mark or board[13] == ' ') and (board[19] == mark or board[19] == ' ')):
        winCounter += 1
        
    if ((board[2] == mark or board[2] == ' ') and (board[14] == mark or board[14] == ' ') and (board[26] == mark or board[26] == ' ')):
        winCounter += 1
    if ((board[8] == mark or board[8] == ' ') and (board[14] == mark or board[14] == ' ') and (board[20] == mark or board[20] == ' ')):
        winCounter += 1
    
    if ((board[3] == mark or board[3] == ' ') and (board[15] == mark or board[15] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1    
    if ((board[9] == mark or board[9] == ' ') and (board[15] == mark or board[15] == ' ') and (board[21] == mark or board[21] == ' ')):
        winCounter += 1  
        
     # diagonal 3d --> 1 14 27; 3 14 25; 9 14 19; 7 14 21
    
    if ((board[1] == mark or board[1] == ' ') and (board[14] == mark or board[14] == ' ') and (board[27] == mark or board[27] == ' ')):
        winCounter += 1  
    if ((board[3] == mark or board[3] == ' ') and (board[14] == mark or board[14] == ' ') and (board[25] == mark or board[25] == ' ')):
        winCounter += 1  
    if ((board[9] == mark or board[9] == ' ') and (board[14] == mark or board[14] == ' ') and (board[19] == mark or board[19] == ' ')):
        winCounter += 1  
    if ((board[7] == mark or board[7] == ' ') and (board[14] == mark or board[14] == ' ') and (board[21] == mark or board[21] == ' ')):
        winCounter += 1  
    
    return winCounter
       



def heuristics():
    heuristic = pseudocheckWIN(board,bot) - pseudocheckWIN(board,player)
    return heuristic

def playerMove():
    position = int(input("Enter your next move: "))
    markMove(player, position)
    return

def botMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            depth = 0
            score = minimax(board,depth,False,-1000,1000)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key

    markMove(bot,bestMove)
    return

def minimax(board, depth, isMax,a ,b):
    alpha = a
    beta = b 
    
    if whoWIN(bot):
        return 1000

    elif whoWIN(player):
        return -1000
    
    elif checkDraw():
        return 0
    if(depth <= 6):   #change the value to adjust difficulty level
        if(isMax):
           
    
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = bot
                    score = minimax(board, depth + 1, False,alpha,beta)
                    board[key] = ' '
                    if(score > alpha):
                        alpha = score
                    
                if alpha>= beta:
                    break
            
            return alpha
    
        else:
            # bestScore = 800
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = player
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[key] = ' '
                    if(score < beta):
                        beta = score
                if(alpha >= beta):
                    break
            return beta
    
    else:
        return heuristics()
        


while not checkWIN():
    botMove()
    playerMove()



# 2d tic tac toe

# board = {1: ' ', 2: ' ', 3: ' ',
#          4: ' ', 5: 'X', 6: ' ',
#          7: ' ', 8: ' ', 9: ' '}

# def showBoard(board):
#     print(board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('--+---+--')
#     print(board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('--+---+--')
#     print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# showBoard(board) 

# def isEmptySpot(position):
#     if (board[position] == ' '):
#         return True
#     else:
#         return False

# def checkDraw():
#     for key in board.keys():
#         if (board[key] == ' '):
#             return False
        
#     return True

# def checkWIN():
#     #rows
#     if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
#         return True
#     elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
#         return True
#     elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
#         return True

#     # columns
#     elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
#         return True
#     elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
#         return True
#     elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
#         return True

#     # diagonal
#     elif (board[1] == board[5] and board[5] == board[9] and board[1] != ' '):
#         return True
#     elif (board[3] == board[5] and board[5] == board[7] and board[3] != ' '):
#         return True
#     else:
#         return False
        
# def whoWIN(mark):
#     #rows
#     if (board[1] == board[2] and board[2] == board[3] and board[1] == mark):
#         return True
#     elif (board[4] == board[5] and board[5] == board[6] and board[4] == mark ):
#         return True
#     elif (board[7] == board[8] and board[8] == board[9] and board[7] == mark ):
#         return True

#     # columns
#     elif (board[1] == board[4] and board[4] == board[7] and board[1] == mark ):
#         return True
#     elif (board[2] == board[5] and board[5] == board[8] and board[2] == mark ):
#         return True
#     elif (board[3] == board[6] and board[6] == board[9] and board[3] == mark ):
#         return True

#     # diagonal
#     elif (board[1] == board[5] and board[5] == board[9] and board[1] == mark ):
#         return True
#     elif (board[3] == board[5] and board[5] == board[7] and board[3] == mark ):
#         return True
#     else:
#         return False

# def markMove (mark,position):

#     if isEmptySpot(position):
#         board[position] = mark
#         showBoard(board)
#         if(checkDraw()):
#             print("Draw")
#             exit()
        
#         if checkWIN() :
#             if mark == 'X':
#                 print("Better luck next time")
#                 exit()
#             else:
#                 print("You win")
#                 exit()
#         return
#     else:
#         print("Not a possible move")
#         position = int(input("Enter another position"))
#         markMove(mark,position)
#         return

# player = 'O'
# bot = 'X'

# def pseudocheckWIN (board, mark):
    
#     winCounter = 0
#     #rows
#     if ((board[1] == mark or board[1] == ' ') and (board[2] == mark or board[2] == ' ') and (board[3] == mark or board[3] == ' ')):
#         winCounter += 1 
#     if ((board[4] == mark or board[4] == ' ') and (board[5] == mark or board[5] == ' ') and (board[6] == mark or board[6] == ' ')):
#         winCounter += 1
#     if ((board[7] == mark or board[7] == ' ') and (board[8] == mark or board[8] == ' ') and (board[9] == mark or board[9] == ' ')):
#         winCounter += 1
        
#     if ((board[1] == mark or board[1] == ' ') and (board[4] == mark or board[4] == ' ') and (board[7] == mark or board[7] == ' ')):
#         winCounter += 1
#     if ((board[2] == mark or board[2] == ' ') and (board[5] == mark or board[5] == ' ') and (board[8] == mark or board[8] == ' ')):
#         winCounter += 1
#     if ((board[3] == mark or board[3] == ' ') and (board[6] == mark or board[6] == ' ') and (board[9] == mark or board[9] == ' ')):
#         winCounter += 1
    
#     if ((board[1] == mark or board[1] == ' ') and (board[5] == mark or board[5] == ' ') and (board[9] == mark or board[9] == ' ')):
#         winCounter += 1
#     if ((board[3] == mark or board[3] == ' ') and (board[5] == mark or board[5] == ' ') and (board[7] == mark or board[9] == ' ')):
#         winCounter += 1
    
#     return winCounter
       



# def heuristics():
#     heuristic = pseudocheckWIN(bot,board) - pseudocheckWIN(player,board)
#     return heuristic

# def playerMove():
#     position = int(input("Enter your next move: "))
#     markMove(player, position)
#     return

# def botMove():
#     bestScore = -1000
#     bestMove = 0

#     for key in board.keys():
#         if (board[key] == ' '):
#             board[key] = bot
#             depth = 0
#             score = minimax(board,depth,False,-1000,1000)
#             board[key] = ' '
#             if(score > bestScore):
#                 bestScore = score
#                 bestMove = key

#     markMove(bot,bestMove)
#     return

# def minimax(board, depth, isMax,a ,b):
#     alpha = a
#     beta = b 
    
#     if whoWIN(bot):
#         return 1

#     elif whoWIN(player):
#         return -1
    
#     elif checkDraw():
#         return 0
#     if(depth <= 6):
#         if(isMax):
#             # bestScore = -1000
    
#             for key in board.keys():
#                 if (board[key] == ' '):
#                     board[key] = bot
#                     score = minimax(board, depth + 1, False,alpha,beta)
#                     board[key] = ' '
#                     if(score > alpha):
#                         alpha = score
                    
#                     if alpha>= beta:
#                         break
            
#             return alpha
    
#         else:
#             # bestScore = 800
#             for key in board.keys():
#                 if (board[key] == ' '):
#                     board[key] = player
#                     score = minimax(board, depth + 1, True, alpha, beta)
#                     board[key] = ' '
#                     if(score < beta):
#                         beta = score
#                     if(alpha >= beta):
#                         break
#             return beta
    
#     else:
#         return heuristics()
        


# while not checkWIN():
#     playerMove()
#     botMove()