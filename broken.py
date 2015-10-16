import curses, time, application
from os import system

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

x = 0
try:
    while x != ord('Q'):
        screen = curses.initscr()

        screen.clear()
        screen.border(0)
        screen.addstr(12, 25, "Python curses in action!")
        screen.addstr(4, 4, "P - Get Current Price")
        screen.addstr(7, 4, "Q - Exit")
        screen.refresh()

        x = screen.getch()

        if x == ord('P'):
            currency_pair = get_param("Enter currency pair (XBTUSD, XBTSGD, XBTEUR): ")
            curses.endwin()
            system('clear')
            while True:
                time.sleep(1)
                print application.get_price('XBTUSD')
                screen.refresh()
except Exception as e:
    exit(1)

curses.endwin()