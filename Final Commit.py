import random
import difflib

def coin_toss():
  return random.choice(['Heads', 'Tails'])

def normalize_input(user_input):
  user_input = user_input.lower().strip()
  
  heads_variations = {"Heads", "heads", "HEADS", "HeadS", "hEADS", "HEaDS", "head", "Head", "HEAD", "hEad", "HeAd",  "hed", "Hed", "HED", "heds", "Heds", "HEDS", "headds", "Headds", "HEADDS", "hads", "Hads", "HADS", "haeds", "Haeds", "HAEDS", "hedas", "Hedas", "HEDAS", "hedz", "Hedz", "HEDZ",  "heafs", "Heafs", "HEAFS", "hesds", "Hesds", "HESDS",  "heqds", "Heqds", "HEQDS",  "headw", "Headw", "HEADW",  "hezds", "Hezds", "HEZDS",  "heaps", "Heaps", "HEAPS",  "hears", "Hears", "HEARS", "hands", "Hands", "HANDS", "Heags", "heags","H", "h"}

  tails_variations = {"Tails", "tails", "TAILS", "TailS", "tAILS", "TAiLS", "tail", "Tail", "TAIL", "tAil", "TaIl",  "tals", "Tals", "TALS", "tils", "Tils", "TILS", "tais", "Tais", "TAIS", "taisl", "Taisl", "TAISL", "tial", "Tial", "TIAL", "tal", "Tal", "TAL",  "tiils", "Tiils", "TIILS", "tials", "Tials", "TIALS", "tailsl", "Tailsl", "TAILSL", "tailsz", "Tailsz", "TAILSZ", "tailz", "Tailz", "TAILZ", "taill", "Taill", "TAILL", "tailsw", "Tailsw", "TAILSW", "tailsx", "Tailsx", "TAILSX", "tailsd", "Tailsd", "TAILSD","t", "T"}

  closest_match = difflib.get_close_matches(user_input, heads_variations | tails_variations, n=1, cutoff=0.75)
  if closest_match:
    return "Heads" if closest_match[0] in heads_variations else "Tails"
  return None
  
def the_player_choice():
    while True:
      user_input = input('Enter your choice (Heads or Tails): ')
      answer = normalize_input(user_input)
      if answer:
        return answer
      print('Invalid choice.Please enter Heads or Tails.')

def play_game():
    player_score = 0
    computer_score = 0
    is_rounds = 7

    print('Welcome To The Coin Toss Game!')
    print(f'There will be {is_rounds} rounds')
    print('The person who gets the most points wins!')
    print('The game will start now!\n')

    for round_num in range(1, is_rounds + 1):
      print(f'Round {round_num}\n')
      
      player_choice = the_player_choice()
      coin_result = coin_toss()

      print(f'You chose: {player_choice}\n')
      print(f'Coin landed on: {coin_result}\n')
    
      if player_choice == coin_result:
        print('You win this round!\n')
        player_score += 1
      else:
        print('Sorry, you chose the wrong side.\n')
        computer_score += 1

      print(f'Player score is {player_score} \nComputer score is {computer_score}\n')

    if player_score > computer_score:
      print(f'Well Done! You won the game!\nThe computer won {computer_score} rounds and you won {player_score} rounds.')
    else:
      print(f'Sorry, you lost the game. \nThe computer won {computer_score} rounds and you won {player_score} rounds.')

if __name__ == "__main__":
    play_game()
