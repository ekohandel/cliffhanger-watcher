import os
import time
import logging
from watcher import Watcher
from notifier import Notifier

logging.basicConfig(format='%(asctime)s %(filename)s: %(message)s')

watcher = Watcher(
    notifier=Notifier(),
    numbers=os.environ['CLIFFHANGER_WATCHER_NUMBERS'].split(';'))

while True:
    try:
        watcher.update()
        time.sleep(int(os.environ['CLIFFHANGER_WATCHER_UPDATE_INTERVAL']))
    except Exception as e:
        logging.error(e)
