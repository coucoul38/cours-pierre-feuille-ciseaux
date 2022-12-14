tabA=[]
def createGrid():
    global tabA
    #on crée x colonnes
    for i in range(3):
        #on crée une ligne de longueur x
        tabB=[]
        for o in range(3):
            #on met un nombre aléatoire dans chaque case de la ligne (0=morte, 1=vivante)
            tabB.append(0)
        #on insère la ligne dans le tableau, créant une colonne
        tabA.append(tabB)

def displayGrid():
    global tabA
    for i in range(3):
        for o in range(3):
            #si la cellule est morte, afficher un carré noir
            if tabA[i][o]==1:
                print("⭕️", end='')
            #si la cellule est morte, afficher un carré blanc
            elif tabA[i][o]==2:
                print("❌",end='')
            else :
                print("⬜", end='')
        #on met une ligne vide, pour mieux différencier chaque grille
        print("", end='\n')

def checkForWin(list):
    col=0
    row=0
    check1=0
    check2=0
    winner = "none"
    #check for horizontal win
    for col in range(3):
        for row in range(3):
            if list[col-1][row-1]==1:
                check1=check1+1
            elif list[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="player1"
            elif check2==3:
                winner="player2"
        check1=0
        check2=0
    #check for vertical wins
    for row in range(3):
        for col in range(3):
            if list[col-1][row-1]==1:
                check1=check1+1
            elif list[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="player1"
            elif check2==3:
                winner="player2"
        check1=0
        check2=0

    #check en bias de gauche à droite
    if list[0][0]==list[1][1]==list[2][2]:
        if list[0][0]==1:
            winner="player1"
        elif list[0][0]==2:
            winner="player2"
    #check en bias de droite à gauche
    if list[0][2]==list[1][1]==list[2][0]:
        if list[0][2]==1:
            winner="player1"
        elif tabA[0][2]==2:
            winner="player2"
    check1 = 0
    check2 = 0

    #check pour egalité
    checkTie = 0
    for i in range(3):
        for o in range(3):
            if list[i][o] != 0 and winner=="none":
                checkTie = checkTie + 1
    if checkTie==9:
        winner="tie"
    return winner

def play(player):
    print("----------")
    print("Joueur ",player,end="")
    if player==1:
        print("⭕️",end="\n")
    if player==2:
        print("❌",end="\n")

    entry=input()
    if entry=="7":
        if(tabA[0][0]==0):
            tabA[0][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="8":
        if(tabA[0][1]==0):
            tabA[0][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="9":
        if(tabA[0][2]==0):
            tabA[0][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="4":
        if(tabA[1][0]==0):
            tabA[1][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="5":
        if(tabA[1][1]==0):
            tabA[1][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="6":
        if(tabA[1][2]==0):
            tabA[1][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="1":
        if(tabA[2][0]==0):
            tabA[2][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="2":
        if(tabA[2][1]==0):
            tabA[2][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="3":
        if(tabA[2][2]==0):
            tabA[2][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    else:
        print("Erreur")
        play(player)

def minimax(isMaximizing):
    if checkForWin(tabA)=="player1":
        return 1
    elif checkForWin(tabA)=="player2":
        return -1
    elif checkForWin(tabA)=="tie":
        return 0

    if isMaximizing:
        bestScore = -100
        for row in range(3):
            for col in range(3):
                if tabA[row][col]==0:
                    tabA[row][col]=1
                    score = minimax(False)
                    tabA[row][col]=0
                    if score > bestScore:
                        bestScore = score
        return bestScore
    elif not isMaximizing:
        bestScore = 100
        for row in range(3):
            for col in range(3):
                if tabA[row][col]==0:
                    tabA[row][col]=2
                    score = minimax(True)
                    tabA[row][col]=0
                    if score < bestScore:
                        bestScore = score
        return bestScore

def botPlay():
    print("----------")
    print("Bot ❌")
    bestScore = 100
    bestMove = [0,0]
    for row in range(3):
        for col in range(3):
            if tabA[row][col]==0:
                tabA[row][col]=2
                score = minimax(True)
                tabA[row][col]=0
                if score < bestScore:
                    bestScore = score
                    bestMove = [row, col]
    tabA[bestMove[0]][bestMove[1]]=2

def ticTacToe(bot=False):
    global tabA
    print("Pour jouer, utilisez les touches du pavé numérique")
    displayGrid()
    while True:
        for i in range(1,3):
            if i==2 and bot==True :
                botPlay()
            else:
                play(i)

            displayGrid()
            if checkForWin(tabA)=="player1":
                print("LE JOUEUR 1 GAGNE! ⭕️")
                print("====================")
                return
            elif checkForWin(tabA)=="player2":
                print("LE JOUEUR 2 GAGNE! ❌")
                print("====================")
                return
            elif checkForWin(tabA)=="tie":
                print("EGALITE!")
                print("====================")
                return

createGrid()
ticTacToe(True)