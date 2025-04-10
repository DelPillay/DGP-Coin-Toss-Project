import random


def coin_toss():
    return random.choice(['Heads', 'Tails'])


def normalize_input(user_input):
    user_input = user_input.lower().strip()

    heads_variations = {"Heads", "heads", "HEADS", "HeadS", "hEADS", "HEaDS", "head", "Head", "HEAD", "hEad", "HeAd",}

    tails_variations = {"Tails", "tails", "TAILS", "TailS", "tAILS", "TAiLS", "tail", "Tail", "TAIL", "tAil", "TaIl",}

    if user_input in heads_variations:
        return "Heads"
    else:
        return "Tails"


def the_player_choice():
    while True:
        user_input = input('Please enter your choice (Heads or Tails): ')
        answer = normalize_input(user_input)
        if answer:
            return answer
        print("\nI Can't Read What Your Input Says, Please Try Again.\n")


def play_game():
        player_score = 0
        computer_score = 0
        is_rounds = 7

        print('Welcome To The Coin Toss Game!')
        print(f'There will be {is_rounds} rounds.')
        print('The person who gets the most points wins!')
        print('The game will start now!')

        for round_num in range(1, is_rounds + 1):
            print(f'Round {round_num}')

            player_choice = the_player_choice()
            coin_result = coin_toss()

            print(f'You chose: {player_choice}')
            print(f'Coin landed on: {coin_result}')

            if player_choice == coin_result:
                print('You win this round!')
                player_score += 1

                print(f'Player score is {player_score} Computer score is {computer_score}')
            else:
                print('Sorry, you chose the wrong side.')
                computer_score += 1

                print(f'Player score is {player_score} Computer score is {computer_score}')

        if player_score > computer_score:
            print(
                f'Well Done! You won the game!The computer won {computer_score} rounds and you won {player_score} rounds.')
        else:
            print(
                f'Sorry, you lost the game. The computer won {computer_score} rounds and you won {player_score} rounds.')



if __name__ == "__main__":
    play_game()
