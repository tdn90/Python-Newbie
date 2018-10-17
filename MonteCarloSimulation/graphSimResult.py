from StatsGenerator import *
import matplotlib.pyplot as plt

def graphResult(games):
    roll_list, win_list, lose_list = tallyResults(games)
    for i in range(len(win_list)):
        # convert raw data to percentage
        win_list[i] = win_list[i] / games * 100
        lose_list[i] = lose_list[i] / games * 100
    plt.plot(roll_list, win_list, label='win')
    plt.plot(roll_list, lose_list, label='lose')
    plt.xlabel('Number of Rolls')
    plt.ylabel('Percentage of win/loss')
    plt.title('Odds of winning or losing for Game of Craps')
    plt.legend()
    plt.show()
    
