import random

def coin_toss():
    return random.choice(['Heads', 'Tails'])

def the_player_choice():
    while True:
        user_input = input('Enter your choice (Heads or Tails): ')
        answer = user_input
        if answer is "Heads" or "Tails":
            return answer
        print('Invalid choice.Please enter Heads or Tails.')


def play_game():
    while True:
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