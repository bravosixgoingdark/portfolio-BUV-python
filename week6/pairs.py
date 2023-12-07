import random

rows1, cols1 = (4, 4) # 4x4 table
rows2, cols2 = (5, 5) # 5x5 table
row = range(rows1) # 0, 1, 2, 3
col = range(cols1) # 0, 1, 2, 3
numOfPairs = 0 # Number of pairs found

#Get a random position for each card
def randomPos():
    rowPos = random.choice(row) # Choose a random number from 0 to 3
    colPos = random.choice(col)     # Choose a random number from 0 to 3

    return rowPos, colPos

#Put 4 of a card into 4 random positions with no overlap
def randomCardPos(x):
    for a in range(4):
        rowPos, colPos = randomPos()
        if cardsPos[rowPos][colPos] != 0:
            while True:
                rowPos, colPos = randomPos()
                if cardsPos[rowPos][colPos] == 0:
                    cardsPos[rowPos][colPos] = x
                    break
        else:
            cardsPos[rowPos][colPos] = x

#Get the first chosen card
def getFirstCard(x):
    firstCardPos = [int(i) for i in x.split() if i.isdigit()]
    print(cardsPos[firstCardPos[0]][firstCardPos[1]])

    return firstCardPos

#Get the second chosen card
def getSecondCard(x):
    secondCardPos = [int(i) for i in x.split() if i.isdigit()]
    print(cardsPos[secondCardPos[0]][secondCardPos[1]])

    return secondCardPos

#Prepare the table with the number of rows and columes
cardsPos = [[0 for i in range(cols1)] for j in range(rows1)]

#Put all the cards into their positions
randomCardPos("Jack")
randomCardPos("Queen")
randomCardPos("King")
randomCardPos("Ace")

#Set up and print the display table
display = [["*" for i in range(cols2)] for j in range(rows2)] # 5x5 table
display[0][0] = " "
for i in range(1,5):
    display[0][i] = "{cord}".format(cord = (i - 1)) # 0, 1, 2, 3, 4
for i in range(1,5):
    display[i][0] = "{cord}".format(cord = (i - 1)) # 0, 1, 2, 3, 4
for row in display:
    print(*row, sep="  ")

while True:
    firstCard = input("Enter the 1st card (row. col): ") # 0, 1, 2, 3, 4
    firstCardPos = getFirstCard(firstCard)
    secondCard = input("Enter the 2nd card (row, col): ") # 0, 1, 2, 3, 4
    secondCardPos = getSecondCard(secondCard)
    
    if display[firstCardPos[0] + 1][firstCardPos[1] + 1] == "X" or display[secondCardPos[0] + 1][secondCardPos[1] + 1] == "X":
        print("Card(s) already paired.")
    elif firstCard == secondCard:
        print("Can't pick the same card.")
    elif cardsPos[firstCardPos[0]][firstCardPos[1]] == cardsPos[secondCardPos[0]][secondCardPos[1]]: # Check if the cards are the same
        numOfPairs += 1 # Increase the number of pairs found
        display[firstCardPos[0] + 1][firstCardPos[1] + 1] = "X" # Replace the card with "X"
        display[secondCardPos[0] + 1][secondCardPos[1] + 1] = "X" # Replace the card with "X"
        print("You found a pair!") # Print the message
        print("Number of pairs found: " + str(numOfPairs)) # Print the number of pairs found
        for row in display: # Print the table
            print(*row, sep="  ")
    else:
        print("Not a match.") # Print the message

    if numOfPairs == 8:
        break