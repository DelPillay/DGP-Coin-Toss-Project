"""This programme runs a heads and tails game against a computer for entertainment.
It has code that will help normalize the input. This mean that if the user types
the answer with a different spelling it will automatically correct itself and will
return the correct answer. It will let the user choose how many rounds that they
want to play. After playing there will be a replay option that will let the user
play again."""

import random
import difflib
import time

MATCH_CUTOFF = 0.75

def coin_toss():
    return random.choice(['Heads', 'Tails'])


def normalize_input(user_input):
    '''Normalize_input is when if the user types the answer but is
    spelt differently it will help correct the statement by replacing
    their answer with the correct one'''
    user_input = user_input.lower().strip()

    heads_variations = {"Heads", "heads", "HEADS", "HeadS", "hEADS",
                        "HEaDS", "head", "Head", "HEAD", "hEad", "HeAd",
                        "hed", "Hed", "HED", "heds", "Heds", "HEDS", 
                        "headds", "Headds", "HEADDS", "hads", "Hads",
                        "HADS", "haeds", "Haeds", "HAEDS", "hedas", 
                        "Hedas", "HEDAS", "hedz", "Hedz", "HEDZ", "heafs",
                        "Heafs", "HEAFS", "hesds", "Hesds", "HESDS",
                        "heqds", "Heqds", "HEQDS", "headw", "Headw",
                        "HEADW", "hezds", "Hezds", "HEZDS", "heaps",
                        "Heaps", "HEAPS", "hears", "Hears", "HEARS",
                        "hands", "Hands", "HANDS", "Heags", "heags",
                        "H", "h"}

    tails_variations = {"Tails", "tails", "TAILS", "TailS", "tAILS",
                        "TAiLS", "tail", "Tail", "TAIL", "tAil", "TaIl",
                        "tals", "Tals", "TALS", "tils", "Tils", "TILS",
                        "tais", "Tais", "TAIS", "taisl", "Taisl",
                        "TAISL", "tial", "Tial", "TIAL", "tal", "Tal",
                        "TAL", "tiils", "Tiils", "TIILS", "tials",
                        "Tials", "TIALS", "tailsl", "Tailsl", "TAILSL",
                        "tailsz", "Tailsz", "TAILSZ", "tailz", "Tailz",
                        "TAILZ", "taill", "Taill", "TAILL", "tailsw", 
                        "Tailsw", "TAILSW", "tailsx", "Tailsx", "TAILSX",
                        "tailsd", "Tailsd", "TAILSD", "t", "T"}
    
    both_variations = heads_variations | tails_variations
    closest_match = difflib.get_close_matches(user_input, both_variations, n=1, cutoff=MATCH_CUTOFF)
    if closest_match:
        return "Heads" if closest_match[0] in heads_variations else "Tails"
    return None


def get_player_choice():
    '''Ask player for choice and gives error message if not Heads or Tails'''
    while True:
        user_input = input('Please enter your choice (Heads or Tails): ')
        answer = normalize_input(user_input)
        if answer:
            return answer
        print("\nI Can't Read What Your Input Says, Please Try Again.\n")


def play_game():
    '''This will Start the game for the user.Then it will ask
    the user for the amount of rounds they want. After playing 
    the programme will calculate the
    amount of rounds that the computer of the player has won.
    It will also tell the player what side the coin has landed'''
    while True:
        print('Welcome To The Coin Toss Game!')
        
        player_score = 0
        computer_score = 0
        
        while True:
            rounds = int(input("How may rounds do you want to play? "))
            if rounds <= 0:
                print("\nPlease enter a number greater than 0.\n")
                time.sleep(0.5)
            else:
                break

        print(f'There will be {rounds} rounds.')
        print('The person who gets the most points wins!')
        print('The game will start now!\n')

        for round_num in range(1, rounds + 1):
            print(f'\n\n\nRound {round_num}\n')

            player_choice = get_player_choice()
            coin_result = coin_toss()

            print(f'You chose: {player_choice}\n')
            print(f'Coin landed on: {coin_result}\n')

            if player_choice == coin_result:
                print('You win this round!\n')
                player_score += 1

                print(f'Player score is {player_score}
                \nComputer score is {computer_score}\n')
                
            else:
                print('Sorry, you chose the wrong side.\n')
                computer_score += 1

                print(f'Player score is {player_score} 
                \nComputer score is {computer_score}\n')

        if player_score > computer_score:
            print(
                f'Well Done! You won the game!\nThe computer won {computer_score} 
                rounds and you won {player_score} rounds.')

        elif player_score == computer_score:
            print("\nIt's a Tie!!!\n")

        else:
            print(
                f'Sorry, you lost the game. \nThe computer won {computer_score}
                rounds and you won {player_score} rounds.')
     
        if not replay_game():
            break

 
def replay_game():
    '''This will ask the user if they want to play the game again.
     If they want to play again it will restart the programme. 
     If they choose to not play again it will thank them for playing.'''

    yes_variations = {"Yes", "yes", "y", "Y", "yeah", "Yeah", "ye", "Ye"}
    no_variations = {"No", "no", "n", "N", "Naw", "naw"}

    while True:
        get_replay_choice = (input("\nDo You Want To Play Again (yes/no)? \n"))

        if get_replay_choice in yes_variations:
            print("\nRestarting The Game Now...\n")
            time.sleep(3)
            return True

        elif get_replay_choice in no_variations:
            print("\nThanks for playing!!!\n")
            return False
            
        else:
            print("\nSorry I can't read that")


if __name__ == "__main__":
    play_game()
