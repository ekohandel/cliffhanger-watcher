import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src'))

from unittest.mock import MagicMock
from watcher import Watcher

class notifier:
    def notify(self):
        print("notified")

def test_run():
    if os.path.exists(Watcher.DATA_FILE):
        os.remove(Watcher.DATA_FILE)

    data_set_one = {
        datetime.datetime(2020, 1, 1, 00, 00): 5,
        datetime.datetime(2020, 1, 2, 00, 00): 4,
        datetime.datetime(2020, 1, 3, 00, 00): 3,
    }
    data_set_two = {
        datetime.datetime(2020, 1, 4, 00, 00): 5,
    }
    n = notifier()
    w = Watcher(notifier=n, numbers=[1, 2, 3])

    w.scraper.getTimes = MagicMock(return_value=data_set_one)
    n.notify = MagicMock()
    w.update()
    n.notify.assert_called_once_with(numbers=[1, 2, 3], body=w.NOTIFICATION_TEXT)

    w.scraper.getTimes = MagicMock(return_value=data_set_one)
    n.notify = MagicMock()
    w.update()
    n.notify.assert_not_called()

    w.scraper.getTimes = MagicMock(return_value=data_set_two)
    n.notify = MagicMock()
    w.update()
    n.notify.assert_any_call(numbers=[1, 2, 3], body=w.NOTIFICATION_TEXT)
