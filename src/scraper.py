import re
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

class Scraper:
    URL = 'https://cliffhangerclimbing.com/core/book/member-booking'

    def _getTimesList(self):
        result = requests.get(Scraper.URL)
        parser = BeautifulSoup(result.text, 'html.parser')
        return [time.text.strip() for time in parser.tbody.find_all('label')]

    def _getTimesFromList(self, times_list):
        times = dict()
        for slot in times_list:
            m = re.match("^(.+ at .+)[\t]{8}\((\\d+) spots available\)", slot)
            times[parse(m.group(1))] = m.group(2)
        
        return times

    def getTimes(self):
        return self._getTimesFromList(self._getTimesList())