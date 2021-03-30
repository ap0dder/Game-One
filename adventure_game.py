import time
import random


def introLA():
    print_pause("You find yourself standing in Skid Row of LA.")
    print_pause("Rumor has it that the Skid Row Druglord ")
    print_pause("is somewhere around here ")
    print_pause("and has been terrorizing LA!")
    print_pause("You are standing on the road. ")
    print_pause("In front of you is an abandoned building.")
    print_pause("To your right is a tent where ")
    print_pause("an ex convict homeless man lives.")


def introNYC():
    print_pause("You find yourself standing in NYC.")
    print_pause("Rumor has it that the Druglord ")
    print_pause("is somewhere around here ")
    print_pause("and has been terrorizing NYC!")
    print_pause("You are standing on the road. ")
    print_pause("In front of you is an abandoned building.")
    print_pause("To your right is a tent where ")
    print_pause("an ex convict homeless man lives.")


def introND():
    print_pause("You find yourself standing in New Delhi.")
    print_pause("Rumor has it that the Druglord ")
    print_pause("is somewhere around here ")
    print_pause("and has been terrorizing New Delhi!")
    print_pause("You are standing on the road. ")
    print_pause("In front of you is an abandoned building.")
    print_pause("To your right is a tent where ")
    print_pause("an ex convict homeless man lives.")


city = random.choice(["LA", "NYC", "New Delhi"])


def intro():
    if city == "LA":
        introLA()
    elif city == "NYC":
        introNYC()
    elif city == "New Delhi":
        introND()
    else:
        introLA()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("(I don't understand this command.\n"
                        "Please choose from the two options provided.)")
    return response


def get_started():
    response = valid_input("Enter 1 to step into the abandoned building.\n"
                           "Enter 2 to step into the homeless man's tent.\n"
                           "What would you like to do?\n",
                           "1", "2")
    if "1" in response:
        print_pause("You have now stepped into the abandoned building!")
        building()
    elif "2" in response:
        print_pause("You have now stepped into the tent.")
        tent()


def building():
    # Things that happen to the player steps into the building
    response = valid_input("The Druglord was waiting "
                           "for you inside the building.\n"
                           "Do you want to fight the Druglord? "
                           "Enter 'YES' to fight or 'NO' to run away.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("OK, you ran away outside the building!")
        get_started()
    elif "yes" in response:
        print_pause("You are courageous! Prepare for battle!")
        fight()


def fight():
    # Things that happen when the player fights
    response = valid_input("The Drugload takes out his gun "
                           "and pulls the trigger on you.\n"
                           "Do you let the bullet hit you on your forehead "
                           "or do you use Captain America's shield?\n"
                           "Enter 'BULLET' to check if you are Superman "
                           "or 'SHIELD' to defend.\n",
                           "bullet", "shield")
    if "bullet" in response:
        print_pause("Sorry, you no Superman.\n"
                    "You hu-man. The bullet hits "
                    "your forehead and you die!\n"
                    "The Drugload wins!")
    elif "shield" in response:
        print_pause("The bullet bounces off the shield "
                    "and hits the Drugload's forehead.\n"
                    "You killed the Drugload!")
    print_pause("GAME OVER!")
    play_again()


def tent():
    # Things that happen to the player steps into the tent
    response = valid_input("The homeless man jumps on you "
                           "and tries to tie you up.\n"
                           "Do you try to run away or fight?\n"
                           "Enter 'RUN' to run out of the tent "
                           "or 'FIGHT' to punch the homeless man.\n",
                           "run", "fight")
    if "run" in response:
        print_pause("OK, you ran out of the tent!")
        get_started()
    elif "fight" in response:
        print_pause("You miss the punch. The homeless man punches you, "
                    "ties you up, takes you inside the building.\n"
                    "He unties you and leaves you in the building.")
        building()


def play_again():
    response = valid_input("Would you like to play again? "
                           "Enter 'YES' or 'NO'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("OK, thank you for playing this game! Goodbye!")
    elif "yes" in response:
        print_pause("Very good, lets take you back "
                    "to another city. Wait to see "
                    "if you end up in NYC, LA, or New Delhi! "
                    "....................")
        intro()
        get_started()


def play_game():
    intro()
    get_started()


play_game()
