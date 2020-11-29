import pickle
from scraper import Scraper
from os import path

class Watcher:
    NOTIFICATION_TEXT = 'Cliffhanger Watcher: New spots are available, better get booking!'
    DATA_FILE = '/data/spots.pickle'
    def __init__(self, notifier, numbers):
        self.scraper = Scraper()
        self.spots = dict()
        if path.exists(Watcher.DATA_FILE):
            with open(Watcher.DATA_FILE, 'rb') as f:
                self.spots = pickle.load(f)
        self.notifier = notifier
        self.numbers = numbers

    def update(self):
        current_spots = self.scraper.getTimes()
        for spot_time in current_spots.keys():
            if spot_time not in self.spots:
                self.notifier.notify(numbers=self.numbers, body=Watcher.NOTIFICATION_TEXT)
                self.spots.update(current_spots)
                with open(Watcher.DATA_FILE, 'wb') as f:
                    pickle.dump(self.spots, f)
                break
