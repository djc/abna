from random import randint
from time import sleep

import settings
from main import Abna2Ynab

if __name__ == '__main__':
    correction = settings.RUN_EVERY_SECONDS * 0.1

    sleep(randint(correction, settings.RUN_EVERY_SECONDS - correction))
    obj = Abna2Ynab()
    obj.run()
