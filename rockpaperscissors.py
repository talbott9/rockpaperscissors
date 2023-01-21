import random
import time

# Converts player command to a number to be used in functions
def convertPlayerCommand(playerCommand):
    if(playerCommand == 'r' or playerCommand.lower() == 'rock'):
        return 0
    elif(playerCommand == 'p' or playerCommand.lower() == 'paper'):
        return 1
    elif(playerCommand == 's' or playerCommand.lower() == 'scissors'):
        return 2
    else:
        return playerCommand # return it unchanged if not r, p or s

# Determines whether player or computer won
def determineWin(playerCommand, computerCommand):
    playerName = 0; computerName = 0;

    if(playerCommand == 0):
        playerName = 'Rock'
    elif(playerCommand == 1):
        playerName = 'Paper'
    elif(playerCommand == 2):
        playerName = 'Scissors'

    if(computerCommand == 0):
        computerName = 'Rock'
    elif(computerCommand == 1):
        computerName = 'Paper'
    elif(computerCommand == 2):
        computerName = 'Scissors'

    print(f'xxxxxxxxxxxxxxxxxxxx\n' 
          f'Player:   {playerName}\nComputer: {computerName}\n'
          f'xxxxxxxxxxxxxxxxxxxx')

    if(playerCommand > computerCommand):
        if(playerCommand != 2 or (playerCommand == 2 and computerCommand == 1)):
            return 1
        else:
            return 0
    elif(playerCommand < computerCommand):
        if(playerCommand == 0 and computerCommand == 2):
            return 1
        else:
            return 0
    else:
        return 2

# More than one of the same play in a row affects computer behaviour
def checkRenzoku(previousCommand, playerCommand, renzoku):
    if(playerCommand == previousCommand):
        if(playerCommand == 0):
            if(not(renzoku[0] >= 3)):
                renzoku[0] += 3
        elif(playerCommand == 1):
            if(not(renzoku[1] >= 3)):
                renzoku[1] += 3
        elif(playerCommand == 2):
            if(not(renzoku[2] >= 3)):
                renzoku[2] += 3
    else:
        renzoku[0] = 0
        renzoku[1] = 0
        renzoku[2] = 0

# This calculates the computer's bias towards playing each element based on the player's choices and then returns one of them
def computerPlay(renzoku):
    RPSChance = [random.randint(0, renzoku[2] + 5), random.randint(0, renzoku[0] + 5), random.randint(0, renzoku[1] + 5)]
    # print(RPSChance)
    # print(renzoku)
    if(RPSChance[0] > RPSChance[1] and RPSChance[0] > RPSChance[2]):
        return 0
    elif(RPSChance[1] > RPSChance[0] and RPSChance[1] > RPSChance[2]):
        return 1
    elif(RPSChance[2] > RPSChance[1] and RPSChance[2] > RPSChance[0]):
        return 2
    else:
        return random.randint(0, 2)

def main():
    playerWins = 0
    computerWins = 0
    playerCommand = 0
    computerCommand = 0
    previousCommand = 9 # stores player's previous play
    renzoku = [0, 0, 0] # checks if the player has made a play more than once

    print('\nWelcome to Rock, Paper, Scissors.\n\nCommands: \'l\': show scoreboard'
          '\n          \'r\', \'p\', \'s\': Play Rock, Paper, or Scissors'
          '\n          \'q\', \'quit\': Quit program\n')

    while playerCommand != 'quit' and playerCommand != 'q':
        computerCommand = computerPlay(renzoku)
        print('\nJanken...')
        playerCommand = input()
        playerCommand = convertPlayerCommand(playerCommand)
        if(playerCommand == 'l'):
            print('\tScoreboard this session\n----------------------------------------\n\tYou:', playerWins, '\t\tI:', computerWins)
        elif(playerCommand == 0 or playerCommand == 1 or playerCommand == 2):
            print('\nHoi!')
            time.sleep(0.5)
            win = determineWin(playerCommand, computerCommand)
            if(win == 1):
                print('You win!')
                playerWins += 1
            elif(win == 0):
                print('You lose...')
                computerWins += 1
            else:
                print('Tie.')
            checkRenzoku(previousCommand, playerCommand, renzoku)
            previousCommand = playerCommand
            time.sleep(1)
        elif(playerCommand == 'q' or playerCommand == 'quit'):
            print('Goodbye.')
            print('\t   Final scoreboard:\n----------------------------------------\n\tYou:', playerWins, '\t\tComputer:', computerWins)
        else:
            pass

main()
