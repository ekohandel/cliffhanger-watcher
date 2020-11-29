import os
import time
from watcher import Watcher
from notifier import Notifier

UPDATE_INTERVAL = 3600

watcher = Watcher(
    notifier=Notifier(),
    numbers=os.environ['CLIFFHANGER_WATCHER_NUMBERS'].split(';'))

while True:
    watcher.update()
    time.sleep(UPDATE_INTERVAL)