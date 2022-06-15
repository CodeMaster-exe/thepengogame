import sys, random, colorama
from time import sleep
from colorama import Fore

cmd_loop = True
print(Fore.RED + "PENGUIN ADVENTURE PRESS A TO BEGIN")
while cmd_loop:
    cmd = input(Fore.CYAN + ">>> ")

    if cmd == "a":
        welcome1 = "Welcome fellow penguin my name is Flappy, press b to continue\n"
        for char in (welcome1):
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif cmd == "b":
        welcome2 = "I just need some information then you will be given further instructions press c to enter the form\n"
        for char in (welcome2):
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
        for char in (welcome4):
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        user = input("Please enter a user name: ")
        welcome5 = "Now is when the Teaching begins press d to start\n"
        for char in (welcome5):
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    #Teaching begins

    elif cmd == "d":
        print("All animations will be disabled. for text.")
        sleep(0.8)
        print("Now you will go to the job hut to get a job type job hut to go")
        sleep(0.5)
    elif cmd == "job hut":
        print("Manager: How may I help you?")
        print(f"{user}: Can I get a job?")
        print('''
        Manager: I have 2 jobs to offer: 
        Job 1: A Community manager
        Job 2: A Money manager
        ''')
        sleep(1)
        hmhy1r = int(input("Which would you like? Job (1) or Job (2)?: "))
        if cmd == 1:
            path1()
        elif cmd == 2:
            path2()


    # paths
    def path1():
        print("hi")

    def path2():
        print("Working on path 2 taking you to path 1 in 3 seconds")
        sleep(3)
        path1()















