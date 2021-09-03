import pyautogui
import random
import time


def click_black():
    """ Here the cursor will click on the color black and then on start game.
        Just remember to let the chat closed and the browser zoom at 100%.
        The clicks are randomized inside the bet box to make it more humanized possible.
    """
    color = random.randint(770, 840)
    color1 = random.randint(340, 350)
    bet = random.randint(-130, -60)
    bet1 = random.randint(65, 95)
    timer = random.randint(4, 9)
    time.sleep(timer)
    pyautogui.moveTo(color, color1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveRel(bet, bet1)
    time.sleep(1)
    pyautogui.click()


def click_red():
    """ Here the cursor will click on the color red and then on start game.
        Just remember to let the chat closed and the browser zoom at 100%.
        The clicks are randomized inside the bet box to make it more humanized possible.
    """
    color = random.randint(580, 650)
    color1 = random.randint(340, 350)
    bet = random.randint(80, 110)
    bet1 = random.randint(65, 95)
    timer = random.randint(4, 9)
    time.sleep(timer)
    pyautogui.moveTo(color, color1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveRel(bet, bet1)
    time.sleep(1)
    pyautogui.click()

