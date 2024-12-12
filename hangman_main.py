from hangman_steps import step_counter
from guess_work import gues_work
import random

WORDS_TO_GUESS = ("symphony", "deactivated", "sultan", "character", "blueprint", "vehicle")

print("\nWelcome to the Hangman game! \n")
print("The rules are simple. You have 6 life points. You can gues 1 letter or the whole word in exchange of 1 life point. \n"
      "If you lose all your health points, the game is over. \n"
      "Good Luck!")
new_game = ""
while True:
    print("\nNew Game? [Y / N]")
    new_game = input()

    if new_game == "Y":
        print("\n")
        print("$$\\   $$\\                               $$\\      $$\\                     ")
        print("$$ |  $$ |                              $$$\\    $$$ |                    ")
        print("$$ |  $$ | $$$$$$\\  $$$$$$$\\   $$$$$$\\  $$$$\\  $$$$ | $$$$$$\\  $$$$$$$\\  ")
        print("$$$$$$$$ | \\____$$\\ $$  __$$\\ $$  __$$\\ $$\\$$\\$$ $$ | \\____$$\\ $$  __$$\\ ")
        print("$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ \\$$$  $$ | $$$$$$$ |$$ |  $$ |")
        print("$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |\\$  /$$ |$$  __$$ |$$ |  $$ |")
        print("$$ |  $$ |\\$$$$$$$ |$$ |  $$ |\\$$$$$$$ |$$ | \\_/ $$ |\\$$$$$$$ |$$ |  $$ |")
        print("\\__|  \\__| \\_______|\\__|  \\__| \\____$$ |\\__|     \\__| \\_______|\\__|  \\__|")
        print("                              $$\\   $$ |                                 ")
        print("                              \\$$$$$$  |                                 ")
        print("                               \\______/                                  ")

        print("\n")

        word_to_guess = random.choice(WORDS_TO_GUESS)
        print(word_to_guess)

        print("==|====|====|====|====|====|== HangMan ==|====|====|====|====|====|==\n")

        for i in word_to_guess:
            print("_ ", end=" ")

        for i in range(0,6):
            step_counter(i)
            win_flag = gues_work(word_to_guess)
            if win_flag:
                break

        if not win_flag:
            print(" $$$$$$\\                                           $$$$$$\\                                 ")
            print("$$  __$$\\                                         $$  __$$\\                                ")
            print("$$ /  \\__| $$$$$$\\  $$$$$$\\$$$$\\   $$$$$$\\        $$ /  $$ |$$\\    $$\\  $$$$$$\\   $$$$$$\\  ")
            print("$$ |$$$$\\  \\____$$\\ $$  _$$  _$$\\ $$  __$$\\       $$ |  $$ |\\$$\\  $$  |$$  __$$\\ $$  __$$\\ ")
            print("$$ |\\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \\$$\\$$  / $$$$$$$$ |$$ |  \\__|")
            print("$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \\$$$  /  $$   ____|$$ |      ")
            print("\\$$$$$$  |\\$$$$$$$ |$$ | $$ | $$ |\\$$$$$$$\\        $$$$$$  |   \\$  /   \\$$$$$$$\\ $$ |      ")
            print(" \\______/  \\_______|\\__| \\__| \\__| \\_______|       \\______/     \\_/     \\_______|\\__|      ")

    else:
        break

print("Thanks for playing.")
print("Bye!!!")
