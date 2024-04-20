def guessing_game():

    import random

    game_number = int(random.randint(1, 100))
    start_message = 'guess a number between 1 and 100'

    game_active = True

    while game_active:

        print(start_message)
        user_guess = int(input())

        if user_guess < game_number:
            print('too low, guess again!')

        elif user_guess > game_number:
            print('too high! guess again')


        elif (user_guess) == (game_number):
            print('Correct!')
            user_input = False
            while user_input is False:
                user_answer = input("Would you like to play again? y/n")
                if str(user_answer) == "y":
                    user_input = True
                    game_active = True
                    game_number = int(random.randint(1, 100))
                elif str(user_answer) == "n":
                    game_active = False
                    user_input = True
                else: print(f"{user_answer} is not a valid input")

guessing_game()
