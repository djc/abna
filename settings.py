import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

ABNA_ACCOUNT = os.getenv('ABNA_ACCOUNT')
ABNA_PASSWORD = os.getenv('ABNA_PASSWORD')
ABNA_PASSNUMBER = os.getenv('ABNA_PASSNUMBER')
YNAB_ACCESS_TOKEN = os.getenv('YNAB_ACCESS_TOKEN')
YNAB_BUDGET_ID = os.getenv('YNAB_BUDGET_ID')
YNAB_ACCOUNT_ID = os.getenv('YNAB_ACCOUNT_ID')

RUN_EVERY_SECONDS = 3600
