# import pandas as pd
# import webbrowser as web

# web.open("https://web.whatsapp.com/send?phone=+526311661632&text=hola")

# time.sleep(5)
# pg.click(1230, 964)
# time.sleep(1)
# pg.press("enter")

# time.sleep(1.5)
# pg.hotkey('ctrl','w')
# time.sleep(1)

import pywhatkit
import time
import pyautogui as pg

pywhatkit.sendwhatmsg_instantly("+526311661632", "Hola mundo")
