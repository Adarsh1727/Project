import glob
from pathlib import Path
from project_bot.utils import load_plug
import logging
from . import bot
from sys import argv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

path = "project_bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        pxt = Path(a.name)
        plugg = pxt.stem
        load_plug(plugg.replace(".py", ""))

print("aadi bot Started & loaded all plugins")

if __name__ == '__main__':
    if len(argv) not in (1,3,4):
        bot.disconnet()
    
    else:
        
        bot.run_until_disconnected()
