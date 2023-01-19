def determineWin(playerCommand, computerCommand):
    playerName = 0; computerName = 0;
    if(playerCommand == 'r'):
        playerCommand = 0;
        playerName = 'Rock'
    elif(playerCommand == 'p'):
        playerCommand = 1;
        playerName = 'Paper'
    elif(playerCommand == 's'):
        playerCommand = 2;
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

import random
playerWins = 0; 
computerWins = 0;
playerCommand = 0;
computerCommand = 0;

print('\nWelcome to Rock, Paper, Scissors.\n\nCommands: \'l\': show scoreboard'
      '\n          \'r\', \'p\', \'s\': Play Rock, Paper, or Scissors'
      '\n          \'q\', \'quit\': Quit program\n')

while playerCommand != 'quit' and playerCommand != 'q':
    computerCommand = random.randint(0, 2);
    print('\nJanken...')
    playerCommand = input()
    if(playerCommand == 'l'):
        print('\tScoreboard this session\n----------------------------------------\n\tYou:', playerWins, '\t\tI:', computerWins)
    elif(playerCommand == 'r' or playerCommand == 'p' or playerCommand == 's'):
        print('\nHoi!')
        win = determineWin(playerCommand, computerCommand)
        if(win == 1):
            print('I lose...')
            playerWins += 1
        elif(win == 0):
            print('I win!')
            computerWins += 1
        else:
            print('Tie.')
    elif(playerCommand == 'q' or playerCommand == 'quit'):
        print('Goodbye.')
    else:
        pass

