import time


print("hello World")


def slow_text(text):
    for char in text:
        print (char, end='')
        time.sleep(.08)



slow_text("Hello Human,")
slow_text("Would you like to play a game?")

