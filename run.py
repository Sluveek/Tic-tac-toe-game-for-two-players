from colorama import Back, Fore, Style
from colorama import init
import pyfiglet

result = pyfiglet.figlet_format("Tic-tac-toe for two players", font="digital")
print(Fore.GREEN + result)

player_scores = {"X": 0, "O": 0}
score_goal = 10


def create(mass):
    print("—" * 13)
    for i in range(3):
        print(f"¦ {mass[0 + i * 3]} ¦ {mass[1 + i * 3]} ¦ {mass[2 + i * 3]} ¦")
        print("—" * 13)


def input_get(choice_player, mass):
    valid = None
    while not valid:
        input_player = input("Where will we put " + choice_player + "? ")
        try:
            input_player = int(input_player)
        except ValueError:
            print("Invalid input. Are you sure you entered a number?")
            continue
        if 1 <= input_player <= 9:
            if str(mass[input_player - 1]) not in "XO":
                mass[input_player - 1] = choice_player
                valid = True
            else:
                print("This cell is already taken!")
        else:
            print("Invalid input. Enter a number from 1 to 9.")


def winTest(mass):
    winString = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))

    for each in winString:
        if mass[each[0]] == mass[each[1]] == mass[each[2]]:
            return mass[each[0]]
    return None


def play_again_prompt():
    while True:
        play_again = input("Do you want to play again? (Yes/No): ")
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            return None
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def main():
    while True:
        mass = list(range(1, 10))
        count = 0
        win = None
        while not win:
            create(mass)
            if count % 2 == 0:
                input_get("X", mass)
            else:
                input_get("O", mass)
            count += 1
            if count >= 4:
                tmp = winTest(mass)
                if tmp:
                    print(tmp, "Won!")

                    # Increase score for the winning player

                    player_scores[tmp] += 1
                    if player_scores[tmp] >= score_goal:
                        print("Game over! Player", tmp, "wins!")
                        if play_again_prompt():
                            break
                        else:
                            return
                    win = True
                    break
            if count == 9:
                print("Equality")
                break
        create(mass)
        print("Scores:")
        for player, score in player_scores.items():
            print("Player", player, "Score:", score)
    main()


main()

input("Press enter to exit!")
