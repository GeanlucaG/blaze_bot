from cursor import click_red, click_black
from last_color import last_color as lc
from color_alert import *


def colors_bet():
    """ This is the part of the program that makes the automatic click on the color,
        allowing you to leave it for up to two hours without danger of being banned.
    """
    query = lc()
    for x in query():
        if x[5] == 'white':
            white_alert()
        elif x[5] == 'red':
            click_red()
        elif x[5] == 'black':
            click_black()

def colors_on_the_screen():
    """ This is the part of the program that opens the popup with the color to bet,
        in this function the bet is made manually.
    """
    query = lc()
    for x in query():
        if x[5] == 'white':
            white_alert()
        elif x[5] == 'red':
            red_alert()
        elif x[5] == 'black':
            black_alert()
