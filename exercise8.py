# Title: Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations 
# to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

while True:
    valid_plays = ['r','p','s']
    
    player_one_play = input('Player 1 play (r (rock), p (paper), s (scissors) or enter q to quit): ')
    if player_one_play == 'q':
        break
    if player_one_play not in valid_plays:
        print('Invalid input. Please try again')
        continue

    player_two_play = input('Player 2 play (r (rock), p (paper), s (scissors) or enter q to quit): ')
    if player_two_play == 'q':
        break
    if player_two_play not in valid_plays:
        print('Invalid input. Please try again')
        continue

    if (player_one_play ==  player_two_play):
        print('Its a draw!')
    elif (player_one_play == 'r' and player_two_play == 's') or (player_one_play == 's' and player_two_play == 'p') or (player_one_play == 'p' and player_two_play == 'r'):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

    play_again = input('Would you like to play again (y/n)? ')
    if play_again == 'n':
        break