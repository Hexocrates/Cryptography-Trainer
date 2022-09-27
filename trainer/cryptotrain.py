import time


print(" ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ")
print("||C |||r |||y |||p |||t |||o |||T |||r |||a |||i |||n |||e |||r ||")
print("||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||")
print("|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")


print(" ____                           __           ______                                           ")
print("/\  _`\                        /\ \__       /\__  _\               __                         ")
print("\ \ \/\_\  _ __   __  __  _____\ \ ,_\   ___\/_/\ \/ _ __    __   /\_\    ___      __   _ __  ")
print(" \ \ \/_/_/\`'__\/\ \/\ \/\ '__`\ \ \/  / __`\ \ \ \/\`'__\/'__`\ \/\ \ /' _ `\  /'__`\/\`'__\'")
print("  \ \ \L\ \ \ \/ \ \ \_\ \ \ \L\ \ \ \_/\ \L\ \ \ \ \ \ \//\ \L\.\_\ \ \/\ \/\ \/\  __/\ \ \/ ")
print("   \ \____/\ \_\  \/`____ \ \ ,__/\ \__\ \____/  \ \_\ \_\\ \__/.\_\\ \_\ \_\ \_\ \____\\ \_\ ")
print("    \/___/  \/_/   `/___/> \ \ \/  \/__/\/___/    \/_/\/_/ \/__/\/_/ \/_/\/_/\/_/\/____/ \/_/ ")
print("                     /\___/\ \_\                                                             ")
print("                     \/__/  \/_/                                                            ") 


def slow_text(text):
    for char in text:
        print (char, end='')
        time.sleep(.08)

def runGame():
    print("Running Game... WIP")

slow_text("Would you like to play a game?: ")
print("Welcome to the Cryptography Trainer, To get started select from either Random mode for a random password or Input Mode to put in your own password")
print("Happy Code Cracking!")
print("")
print("Please Select a Mode")
print("0 - Random Password Mode")
print("1 - Input Mode")
print("2 - Exit ")
mode = input("")
if (mode == "0" or mode == "1"):
    print(f"Selected mode {mode} : Processing....")
    runGame()
elif  (mode == "2"):
    slow_text("Goodbye... Exiting")
else:
    print("Invalid Choice... Exiting ")
