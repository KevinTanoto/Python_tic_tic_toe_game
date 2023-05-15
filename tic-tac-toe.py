def gameBoard():
    for n, i in enumerate(list):
        print(' --- '  * 3 + ' ')
        for m, j in enumerate(list[n]):
            print('| '+ str(list[n][m]) +' ' +'|' , end = '')
        print()
    print(' --- '  * 3 + ' ')

def nextPlayer():
    player = 1
    answer = 'X' 
    for i in range(9):
        inp = str(input('Player ' + str(player) + ' Your Move is (row 1-3,column 1-3): '))
        inplist = inp.split(',')
        inplist = [int(i) for i in inplist]
        if player == 1:
            if list[inplist[0]-1][inplist[1]-1] is 0:
                list[inplist[0]-1][inplist[1]-1] = answer
                winner = TTTwinCheck(list)
                if winner != 3:
                    gameBoard()
                    print('The Winner is Player ' + str(player))
                    break
                else:
                    player = 2
                    answer = 'O'
                    gameBoard()
                    continue
            else:
                print('The spot is taken')
                continue 
        if player == 2:
            if list[inplist[0]-1][inplist[1]-1] is 0:
                list[inplist[0]-1][inplist[1]-1] = answer
                winner = TTTwinCheck(list)
                if winner != 3:
                    gameBoard()
                    print('The Winner is Player ' + str(winner))
                    break
                else:
                    player = 1
                    answer = 'X'
                    gameBoard()
                    continue
            else:
                print('The spot is taken')
                continue
    print('Draw ')                

def TTTwinCheck(list):
    #horizontal
    listH = []
    listH2 = []
    for m, j in enumerate(list):
        countH = 0
        for n, i in enumerate(list[m]):
            if list[m][n] == list[m][n-1] and list[m][n] == 'X':
                countH +=1
                listH.append(countH)
            if list[m][n] == list[m][n-1] and list[m][n] == 'O':
                countH +=1
                listH2.append(countH)
    #vertical
    listV = [] 
    listV2 = []
    for m, j in enumerate(list):
        countV =0
        for n, i in enumerate(list[m]):
            if list[n][m] == list[n-1][m] and list[n][m] == 'X':
                countV +=1
                listV.append(countV)
            if list[n][m] == list[n-1][m] and list[n][m] == 'O':
                countV +=1
                listV2.append(countV)
    #diagonal
    countD = 0 
    countDD = 0
    countD2 = 0 
    countDD2 = 0
    for n, i in enumerate(list):
        if list[n][n] == list[n-1][n-1] and list[n][n] == 'X':
            countD += 1
        elif list[n][-(n+1)] == list [n-1][-(n+1)+1] and list[n][-(n+1)] == 'X':
            countDD +=1
        if list[n][n] == list[n-1][n-1] and list[n][n] == 'O':
            countD2 += 1
        elif list[n][-(n+1)] == list [n-1][-(n+1)+1] and list[n][-(n+1)] == 'O':
            countDD2 +=1
    
    if countDD == 3 or countD == 3 or 3 in listH or 3 in listV:
        winner = 1
    elif countDD2 == 3 or countD2 == 3 or 3 in listH2 or 3 in listV2:
        winner = 2
    else:
        winner = 3

    return winner


if __name__== '__main__':
    print('Welcome to Tic Tac Toe Game')
    while True:
        list = [
            [0,0,0],
            [0,0,0],
            [0,0,0]]
        print()
        print('1. Play')
        print('2. Exit')
        inp = int(input('Input: '))
        if inp == 1:
            gameBoard()
            nextPlayer()
            continue
        elif inp == 2:
            break
        else:
            continue



