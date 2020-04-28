import datetime
import random

NAMES = [
    'Anna', 'Bartosz', 'Celina', 'Damian', 'Elzbieta', 'Feliks', 'Grazyna', 'Halina', 'Ignacy', 'Jerzy',
    'Karol', 'Lucjan', 'Maria', 'Norbert', 'Olgierd', 'Piotr', 'Ramona', 'Sylwia', 'Tadeusz', 'Urszula',
    'Wladyslaw', 'Zofia'
]
SURNAMES = [
    'Alba', 'Baran', 'Czech', 'Dab', 'Ekler', 'Florek', 'Gora', 'Hak', 'Igla', 'Jantar', 'Kot', 'Lipa',
    'Maka', 'Oko', 'Pilot', 'Rumak', 'Sek', 'Trok', 'Uran', 'Wrona', 'Zajac'
]


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.date(year=1901, month=1, day=1)
    end = datetime.date(year=2001, month=12, day=31)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def random_name():
    return random.choice(NAMES)


def random_surname():
    return random.choice(SURNAMES)

import time


class Timer:
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
        print(f'----{self.name}---- \n time {self.interval}')
