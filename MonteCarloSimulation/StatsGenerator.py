from GameOfCrap import *

def processData(statusList, rolls, size):
    x_list = []
    win_list = []
    lose_list = []
    maxRoll = max(rolls)
    for i in range(maxRoll+1):
        x_list.append(i)
        win_list.append(0)
        lose_list.append(0)
    for j in range(size):
        # victory! Then update win_list
        if (statusList[j]):
            win_list[rolls[j]] += 1
        else: # uh oh it's a loss... update lose_list
            lose_list[rolls[j]] += 1
    return x_list, win_list, lose_list


def tallyResults(games):
    statusList = []
    rolls = []
    for i in range(games):
        status, roll = playOneGame()
        statusList.append(status)
        rolls.append(roll)
    roll_list, win_list, lose_list = processData(statusList, rolls, games)
    return roll_list, win_list, lose_list
        
