import os
import time
from watcher import Watcher
from notifier import Notifier

watcher = Watcher(
    notifier=Notifier(),
    numbers=os.environ['CLIFFHANGER_WATCHER_NUMBERS'].split(';'))

while True:
    watcher.update()
    time.sleep(int(os.environ['CLIFFHANGER_WATCHER_UPDATE_INTERVAL']))