import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


def get_account_mapping():
    i = 0
    result = {}
    while True:
        i += 1
        iban = os.getenv('ABNA_IBAN_{}'.format(i))
        account = os.getenv('YNAB_ACCOUNT_{}'.format(i))
        if not all([iban, account]):
            break
        result[iban] = account
    return result


ABNA_ACCOUNT = os.getenv('ABNA_ACCOUNT')
ABNA_PASSWORD = os.getenv('ABNA_PASSWORD')
ABNA_PASSNUMBER = os.getenv('ABNA_PASSNUMBER')
YNAB_ACCESS_TOKEN = os.getenv('YNAB_ACCESS_TOKEN')
YNAB_BUDGET_ID = os.getenv('YNAB_BUDGET_ID')
ACCOUNTS = get_account_mapping()

RUN_EVERY_SECONDS = 3600
