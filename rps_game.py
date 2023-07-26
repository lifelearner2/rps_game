"""
Rock, Paper, Scissors Game:
Develop a Python program that allows a user to play the classic game of rock, paper, scissors against the computer. The program should prompt the user to choose either rock, paper, or scissors, and then generate a random choice for the computer. Determine the winner based on the game's rules (rock beats scissors, paper beats rock, scissors beat paper), and display the result to the user.
Additionally, keep track of the user's and computer's scores and provide an option to play multiple rounds until the user decides to quit.
"""
import random

#Randomly select Rock, Paper, Scissors for player1 and player2
def choose_rps():
  "output: randomly returns rock, paper or scissors"
  r = random.randint(0,2)
  if r == 0:
    return "rock"
  elif r == 1:
    return "scissors"
  else:
    return "paper"

#Determine the winner using Rock Paper Scissors function
def rps(player1, player2):
  #tie
  if player1 == player2:
    print("It's a tie!")
  #player 1 = rock
  elif player1 == 'rock':
    if player2 == 'paper':
      print("Paper covers Rock! Player 2 wins!")
    elif player2 == 'scissors':
      print("Rock breaks Scissors! Player 1 wins!")
  #player 1 = paper
  elif player1 == 'paper':
    if player2 =='rock':
      print("Paper covers Rock! Player 1 wins!")
  #player 1 = scissors
  elif player1 == 'scissors':
    if player2 == 'rock':
      print("Rock breaks Scissors! Player 2 wins! ")
    elif player2 == 'paper':
      print("Scissors cut Paper! Player 1 wins!")
  #invalid input - this will print a message if invalid input is put in for any particular player
  else:
        print("Invalid input, Game can not run")

# print("Test run of the game: ")
# rps('rock', 'rock')
# rps('rock', 'paper')
# rps('rock', 'scissors')
# rps('scissors', 'rock')
# rps('paper', 'rock')
# rps('scissors', 'paper')
# rps('book', 'pencil')
# rps('paper', 'pencil')
# rps('pencil', 'paper')

def rps_score(player1, player2, player1score, player2score):
  if player1 == player2:
        pass  # It's a tie, so no score update needed
  elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (
            player1 == 'scissors' and player2 == 'paper'):
        player1score += 1  # Player 1 wins
  else:
        player2score += 1  # Player 2 wins

  return player1score, player2score

def play_game():
  player1score = 0
  player2score = 0

  while True:
      print()
      play = int(input("Type 0 if you want to play or 1 to exit game:"))
      if play == 0:
        print()
        player1 = input("Enter your choice (rock, paper or scissors - lowercase letters only): ")
        player2 = choose_rps()
        print()
        print(f"You chose: ", player1)
        print(f"Computer chose: ", player2)
        rps(player1, player2)  # Check and print the winner
        player1score, player2score = rps_score(player1, player2, player1score, player2score)  # Update scores
        print()
        print("Your Score:", player1score)
        print("Computer Score:", player2score)
      else:
        print()
        print("Thank you for playing!")
        break

play_game()

















