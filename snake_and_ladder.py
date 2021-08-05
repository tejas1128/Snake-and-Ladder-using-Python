import random

snake = {17:7, 62:19, 87:24, 54:34, 64:60, 98:79, 95:75, 93:73}
ladder = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 80:100, 71:91}

def makeMove():

    num = random.randint(1,6)

    if num==1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    elif num==2:
        print("---------")
        print("|   *   |")
        print("|       |")
        print("|   *   |")
        print("---------")
    elif num==3:
        print("---------")
        print("|   *   |")
        print("|   *   |")
        print("|   *   |")
        print("---------")
    elif num==4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    elif num==5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    elif num==6:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")

    return num
    

def playerTurn(name, place, i):
    print("\n\n\nYour Turn :", name)
    nameLength = len(name)
    guessCorrect = False
    print("Current position : " + str(place) + "\n")

    while(not guessCorrect):
        temp = random.randint(0, nameLength-1)
        tempLetter = name[temp]

        question = "Enter "+ str(temp+1) +"th letter of your name : ";
        tempInput = input(question)

        if(tempInput == tempLetter):
            guessCorrect = True

        else:
            print("======  WRONG GUESS  ======");
            guessCorrect = False

    inc = 0

    num = makeMove()
    if(num == 6):
        i -= 1;
        inc = 1;
        print("The next turn is also your's")

    x = place + num
    if (x in snake.keys()):
        print("OHH oooohh. You are bitten by the sanke :(")
        place = snake[x]
        print("You are now at :", place)
        

    elif (x in ladder.keys()):
        print("Wah, You climed the ladder :) ")
        place = ladder[x]
        print("You are now at :", place)
        print("The next turn is also your's, :)")

        if (inc != 1) :  # to avoid multiple decrement if the dies show up 6
            i -= 1

    elif (x > 100):
        place = place

    else:
        place = x;
        print("You are now at :", place)

    return (place, i)

def play():

    name1 = input("Enter player 1 name: ").strip().capitalize()
    temp = name1.split()
    name1 = temp[0];
    print("===========  NOTE ::: ->  Your name is taken as '" + name1 + "'\n\n");
    name2 = input("Enter player 2 name: ").strip().capitalize()
    temp = name2.split()
    name2 = temp[0];
    print("===========  NOTE ::: ->  Your name is taken as '" + name2 + "'");

    player1place = 0
    player2place = 0
    notWin = True

    i = 0
    while(notWin):

        if(i%2 == 0):
            (player1place, i) = playerTurn(name1, player1place, i)

            if(player1place == 100):
                print("Hurray... You (" + name1 + ") are the winner :) :>")
                notWin = False;

        else:
            (player2place, i) = playerTurn(name2, player2place, i)

            if(player2place == 100):
                print("Hurray... You (" + name2 + ") are the winner :) :>")
                notWin = False;

        i += 1

play()
