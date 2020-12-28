import re
import requests
import sys
from bs4 import BeautifulSoup
from dateutil.parser import parse

class Scraper:
    URL = 'https://cliffhangerclimbing.com/core/book/member-booking'

    def _getTimesList(self):
        time_list = []
        try:
            result = requests.get(Scraper.URL)
            parser = BeautifulSoup(result.text, 'html.parser')
            time_list = [time.text.strip() for time in parser.tbody.find_all('label')]
        except ConnectionError as e:
            print(e, file=sys.stderr)

        return time_list

    def _getTimesFromList(self, times_list):
        times = dict()
        for slot in times_list:
            m = re.match("^(.+ at .+)[\t]{8}\((\\d+) spots available\)", slot)
            times[parse(m.group(1))] = m.group(2)
        
        return times

    def getTimes(self):
        return self._getTimesFromList(self._getTimesList())