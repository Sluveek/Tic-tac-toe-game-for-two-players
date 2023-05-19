from colorama import just_fix_windows_console
from colorama import Back, Fore, Style
from colorama import init

print(Fore.RED + "*" * 10, " Tic-tac-toe game for two players ", "*" * 10)


table = list(range(1, 10))

def table_draw(table):
    print("—" * 13)
    for i in range(3):
        print("¦", table[0 + i * 3], "¦", table[1 + i * 3], "¦", table[2 + i * 3],"¦")
        print("—" * 13)

def input_get(choice_player):
    valid = False
    while not valid:
        input_player = input("Where will we put " + choice_player + "? ")
        try:
            input_player = int(input_player)
        except ValueError:
            print("Invalid input. Are you sure you entered a number?")
            continue
        if 1 <= input_player <= 9:
            if str(table[input_player - 1]) not in "XO":
                table[input_player - 1] = choice_player
                valid = True
            else:
                print("This cell is already taken!")
        else:
            print("Invalid input. Enter a number from 1 to 9.")

def winTest(table):
    winString = ((0,1,2 ), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in winString:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False

def main(table):
    counter = 0
    win = False
    while not win:
        table_draw(table)
        if counter % 2 == 0:
            input_get("X")
        else:
            input_get("O")
        counter += 1
        if counter >= 4:
            tmp = winTest(table)
            if tmp:
                print(tmp, "Won!")
                win = True
                break

        if counter == 9:
            print("Equality")
            break
    table_draw(table)

main(table)

input("Press enter to exit!")