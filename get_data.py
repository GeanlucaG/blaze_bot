from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from bot_blaze import colors_bet, colors_on_the_screen
from last_color import sqlconnect
import datetime
import time


def insert_db(color, number, time):
    """ Insert the data collected from 'blaze.com/pt/games/double' into the db.
        Update the column names from the SELECT and INSERT, otherwise it won't work.
    """
    mydb = sqlconnect()
    query = mydb.cursor()
    query.execute("SELECT id FROM rolldice_tbo WHERE number = %s AND datetime = '%s'" % (number, str(time)))
    result = query.fetchone()

    if result == None:
        sql = "INSERT INTO rolldice_tbo (color,number,datetime) VALUES (?, ?, ?)"
        val = (color, number, str(time))
        query.execute(sql, val)
        mydb.commit()

    elif result == None:
        sql = "INSERT INTO rolldice_tbo (color,number,datetime) VALUES (?, ?, ?)"
        val = (color, number, str(time))
        query.execute(sql, val)
        mydb.commit()


def get_data():
    """
    This function collects information from the website.
    In this case, the columns: Color, Number, Time.
    Here are needed two things downloaded: The Mozilla Firefox and the Geckodriver.exe.
    If you want to the bot can bet for you. It's just uncomment the line 53 and open the blaze website.
    Just keep in mind one thing, always keep your chat closed and the zoom of your browser at 100%,
    otherwise the bot will missclick the colors.
    If you don't want the bot to bet for you, just uncomment the line 54 and you can do it manually.
    It will appear one popup with the color instruction.
    """
    browser = Firefox(executable_path=r"C:\selenium\geckodriver.exe")
    browser.get("https://blaze.com/pt/games/double")
    first = True
    time.sleep(3)

    while True:
        roulette_timer = (By.CSS_SELECTOR, "#roulette-timer")
        roulette = browser.find_element(*roulette_timer).get_attribute('innerHTML')
        qtd = len(roulette.split('"time-left">Blaze Girou <b>'))

        if qtd == 2:
            time.sleep(3)
            #colors_bet()
            #colors_on_the_screen()
            if first:
                time.sleep(2)
                locator = (By.CSS_SELECTOR, ".roulette-previous")
                numbers = (browser.find_element(*locator).get_attribute('innerHTML'))
                now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

                numbers = numbers.split('class="roulette-tile"><div class="sm-box ')
                num = numbers[1]
                color = (num.split('">'))[0]
                if color == "white":
                    number = 0
                    print(color, number, now)
                else:
                    number = (num.split('class="number">'))
                    number = number[1].split("</div>")
                    number = number[0]
                    print(color, number, now)
                first = False
        else:
            first = True

if __name__ == '__main__':
    get_data()