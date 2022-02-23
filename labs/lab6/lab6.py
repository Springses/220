"""
Elijah Springs

lab6.py

This program creates a key based on user input.

This is my work.
"""

from graphics import *

def vigenere():
    # the window
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0,0,10,10)

    # a white background for those who have a macbook in dark mode
    background = Rectangle(Point(0,0), Point(10,10))
    background.setFill("white")
    background.draw(win)

    # input text
    message_text = Text(Point(2.5, 8.5), "Message to code")
    message_text.draw(win)
    key_text = Text(Point(2.5, 7.5), "Enter keyword")
    key_text.draw(win)

    # inputs
    message_entry = Entry(Point(6, 8.5), 25)
    key_entry = Entry(Point(6, 7.5), 20)
    message_entry.draw(win)
    key_entry.draw(win)

    # 'button'
    button = Rectangle(Point(3, 4), Point(7, 6))
    button_text = Text(button.getCenter(), "ENCODE")
    button.draw(win)
    button_text.draw(win)

    # get text and undraw button
    win.getMouse()
    message = message_entry.getText()
    key = key_entry.getText()
    button.undraw()
    button_text.undraw()

    # replacing spaces and capitalizing the letters
    message = message.replace(" ", "")
    message = message.upper()
    key = key.replace(" ", "")
    key = key.upper()

    # string accumulator
    new_key= ""

    # loop
    for i in range(len(message)):

        # indexing
        mes_letter = message[i]
        key_letter = key[i % len(key)]

        # converting letters to numbers
        mes_ord = ord(mes_letter)
        key_ord = ord(key_letter)

        # subtracting numbers
        mes_accumulator = mes_ord - 65
        key_accumulator = key_ord - 65

        # calculating new letters
        new_ord = (mes_accumulator + key_accumulator) % 26
        new_chr = new_ord + 65
        new_letter = chr(new_chr)

        # the new key
        new_key = new_key + new_letter
        new_key = new_key.upper()

    # outputs
    new_key_text = Text(Point(5, 4), new_key)
    new_key_text.draw(win)
    resulting_text = Text(Point(5, 5), "Resulting message:")
    resulting_text.draw(win)

    # closing instructions
    closing_text = Text(Point(5, 2), "Click again to close")
    closing_text.draw(win)
    win.getMouse()
    win.close()
