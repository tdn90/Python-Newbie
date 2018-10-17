from random import randrange, seed

def roll():
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    return dice1 + dice2

def playOneGame():
    victory = True
    rolls = 0
    initRoll = roll()
    rolls += 1
    # Player wins if first roll is either 7 or 11
    if initRoll == 7 or initRoll == 11:
        pass
        # do nothing here, already win
        # Player loses if first roll is 2, 3 or 12
    elif initRoll == 2 or initRoll == 3 or initRoll == 12:
        victory = False
    else:
        currentRoll = -1
        # Roll until either a 7 or value of initial roll appears
        while not(currentRoll == 7 or currentRoll == initRoll):
            currentRoll = roll()
            rolls += 1
        # If a 7 appears first, player loses
        if currentRoll == 7:
            victory = False
        # If initial roll appears again first, player wins - no update necessary
    return victory, rolls
        
