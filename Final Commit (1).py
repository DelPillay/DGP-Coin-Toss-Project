import random
import difflib
import time


yes_variations = {"Yes", "yes", "y", "Y", "yeah", "Yeah", "ye", "Ye"}
MATCH_CUTOFF = 0.75

def coin_toss():
    return random.choice(['Heads', 'Tails'])


def normalize_input(user_input):
    user_input = user_input.lower().strip()

    heads_variations = {"Heads", "heads", "HEADS", "HeadS", "hEADS", "HEaDS", "head", "Head", "HEAD", "hEad", "HeAd",
                        "hed", "Hed", "HED", "heds", "Heds", "HEDS", "headds", "Headds", "HEADDS", "hads", "Hads",
                        "HADS", "haeds", "Haeds", "HAEDS", "hedas", "Hedas", "HEDAS", "hedz", "Hedz", "HEDZ", "heafs",
                        "Heafs", "HEAFS", "hesds", "Hesds", "HESDS", "heqds", "Heqds", "HEQDS", "headw", "Headw",
                        "HEADW", "hezds", "Hezds", "HEZDS", "heaps", "Heaps", "HEAPS", "hears", "Hears", "HEARS",
                        "hands", "Hands", "HANDS", "Heags", "heags", "H", "h"}

    tails_variations = {"Tails", "tails", "TAILS", "TailS", "tAILS", "TAiLS", "tail", "Tail", "TAIL", "tAil", "TaIl",
                        "tals", "Tals", "TALS", "tils", "Tils", "TILS", "tais", "Tais", "TAIS", "taisl", "Taisl",
                        "TAISL", "tial", "Tial", "TIAL", "tal", "Tal", "TAL", "tiils", "Tiils", "TIILS", "tials",
                        "Tials", "TIALS", "tailsl", "Tailsl", "TAILSL", "tailsz", "Tailsz", "TAILSZ", "tailz", "Tailz",
                        "TAILZ", "taill", "Taill", "TAILL", "tailsw", "Tailsw", "TAILSW", "tailsx", "Tailsx", "TAILSX",
                        "tailsd", "Tailsd", "TAILSD", "t", "T"}
    
    both_variations = heads_variations | tails_variations
    closest_match = difflib.get_close_matches(user_input, both_variations, n=1, cutoff=MATCH_CUTOFF)
    if closest_match:
        return "Heads" if closest_match[0] in heads_variations else "Tails"
    return None


def get_player_choice():
    while True:
        user_input = input('Please enter your choice (Heads or Tails): ')
        answer = normalize_input(user_input)
        if answer:
            return answer
        print("\nI Can't Read What Your Input Says, Please Try Again.\n")


def play_game():
    while True:
        print('Welcome To The Coin Toss Game!')
        player_score = 0
        computer_score = 0
        rounds = int(input("How may round do you want to play? "))

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

                print(f'Player score is {player_score} \nComputer score is {computer_score}\n')
                
            else:
                print('Sorry, you chose the wrong side.\n')
                computer_score += 1

                print(f'Player score is {player_score} \nComputer score is {computer_score}\n')

        if player_score > computer_score:
            print(
                f'Well Done! You won the game!\nThe computer won {computer_score} rounds and you won {player_score} rounds.')

        else:
            print(
                f'Sorry, you lost the game. \nThe computer won {computer_score} rounds and you won {player_score} rounds.')

        replay_game = (input("\nDo You Want To Play Again (yes/no)? \n"))

        if replay_game not in yes_variations:
            print("\nThanks for playing my game!")
            break

        else:
            print("\nRestarting The Game Now...\n")
            time.sleep(3)


if __name__ == "__main__":
    play_game()
