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



slow_text("Hello Human,")
slow_text("Would you like to play a game?")

