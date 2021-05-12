import telepot
from time import sleep
bot = telepot.bot('token')
bot.driver.get('token')
while True:
    elemt = bot.find_element_by_line_text('http://gestyy.com/eeGK6X')
    elemt.click

    sleep(30)
