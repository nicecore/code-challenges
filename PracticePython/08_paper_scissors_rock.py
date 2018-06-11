import replit

CHOICES = ['Rock', 'Paper', 'Scissors']

def main():
  """Main game function"""
  (player1, player2) = player_select()

def cls():
  """Clear screen"""
  replit.clear()


def player_select():
  """Receive input from each player, store names in a tuple of
  two strings"""
  player1 = input("Player 1, please enter your name:\n> ")
  cls()
  player2 = input(
    "Thanks, {}! Player 2, now enter your name:\n> ".format(player1)
  )
  cls()
  return player1, player2





# Ask if player wants to face off against the computer or another player?
# If computer, proceed to vs. computer stuff
# Otherwise, proceed as two human players



