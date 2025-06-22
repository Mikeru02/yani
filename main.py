# Main Module of YANI
from command import *

if __name__ == "__main__":
    cls = Clear_Screen()
    running = True

    # Start looping
    while running:
        # Ask for language
        print("YANI is ready select language\n\n[A] Gen Z\n[B] Normal\n[C] Exit")
        choice = input("\n>> ")

        if choice.lower() == 'a':
            file = Open_File("data/genz.json").execute()
            description = f"Wazzup pipz! I'm \"YANI\", Your AI Navigator and Informant"
            message = f"Want some rizz rn?\n"
            delay = 1
            cls.execute()
            Greet_User(description, message, delay).execute()
            Conversation(file).execute()
            break
        elif choice.lower() == 'b':
            file = Open_File("data/normal.json").execute()
            description = f"Hello I am \"YANI\", Your AI Navigator and Informant"
            message = f"How can I assists you?\n"
            delay = 1
            cls.execute()
            Greet_User(description, message, delay).execute()
            Conversation(file).execute()
            break
        elif choice.lower() == 'c':
            running = False
        else:
            print("Invalid choise press [ENTER] to continue")
            input()
            cls.execute()
