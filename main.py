import sys
import colorama
from time import sleep
from colorama import Fore

cmd_loop = True
print(Fore.RED + "PENGUIN ADVENTURE PRESS A TO BEGIN")
while cmd_loop:
    cmd = input(Fore.CYAN + ">>> ")

    if cmd == "a":
        welcome1 = "Welcome fellow penguin my name is Flappy, press b to continue\n"
        for char in welcome1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif cmd == "b":
        welcome2 = "I just need some information then you will be given further instructions press c to enter the " \
                   "form\n "
        for char in welcome2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif cmd == "c":
        name = input("What is your name ?: ")
        age = int(input("What is your age (please no decimals)?: "))
        name = name.upper()
        if age < 10:
            print("You are too young to play a game. Discontinuing in 5 seconds.")
            sleep(5)
            break
        welcome4 = "Now you will be prompted to enter some info\n"
        for char in welcome4:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        user = input("Please enter a user name: ")
        welcome5 = "Now is when the Teaching begins press d to start\n"
        for char in welcome5:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    # Teaching begins

    elif cmd == "d":
        print("All animations will be disabled. for text.")
        sleep(0.8)
        print("Now you will go to the job hut to get a job type job hut to go")
        sleep(0.5)
    elif cmd == "job hut":
        print("Manager: How may I help you?")
        print(f"{user}: Can I get a job?")
        print(Fore.CYAN + '''
        Manager: I have 2 jobs to offer: 
        Job 1: A Community manager
        Job 2: A Money manager
        ''')
        sleep(1)
        hmhy1r = int(input("Which would you like? Job (1) or Job (2)?: "))
        if hmhy1r == 1:
            path1()
        elif hmhy1r == 2:
            path2()

    # paths
    def path1():
        coins = 0
        gem = 0
        print("Welcome to community manager.")
        sleep(0.5)
        print('''
        Here are the commands you can type c-cmds to access the full list.
        Shop
        C-Stats
        balance
        eco
        ''')
        print("Type start")
        if cmd == "start":
            print(f'''Welcome {user} I will give you 10 coins to start off.
            you can always type balance to check your coins
            ''')
            sleep(1.5)
            coins = coins + 10
            print("You can also type shop to see what I have to offer")
            sleep(1)
            print("To see community stats type C-Stats")
            sleep(1)
            print("To check eco type eco")
        elif cmd == "shop":
            print(Fore.LIGHTBLUE_EX + "The Shop" +
                  '''
                  Daily Free gems (possible gems 0-5) (1 min cooldown)- type gem-gift - FREE
                  Small House - makes homeless people less and eco better - type small-house - 5 coins
                  Port - Provides fish and less hunger and more eco - type b-port - 500 coins
                  Bank - Gives you money by investing in stocks and better eco- type b-bank - 1500 coins and 10 gems
                  Big House - makes homeless people go down by alot and eco better - type b-house - 10000 coins
                  ''')
        elif cmd == "balance":
            print(f"you have {coins} coins.")
            print(f"Yo have {gem} gems")



    def path2():
        print("Working on path 2 taking you to path 1 in 3 seconds")
        sleep(3)
        path1()
