# ABN2YNAB

This script is made to add your transactions from ABN AMRO to YNAB application

### How it works?
There is no officiall ABN AMRO's API. That is why, this repository is using https://github.com/djc/abna.git to get transactions. It is included in `requirements.txt` file.
Use this application at your own risk.

With this API the application gets 20 latest transactions for each account and store it at YNAB with `import_id` equal to `"ABNAMRO:<transaction_timestamp>"`. (Check [documentation](https://api.youneedabudget.com/v1#/Transactions/createTransaction) to get know why it is needed).
At the end of the run, application will store last transaction timestamps at `last_transactions.json` per each account. Only the transactions after those, will be processed at the next run.

After successful run, your transactions will appear at YNAB. But they need to be confirmed by you. YNAB connects imported transactions to existing ones if amount is equal.
At **Manage Payees** form you can arrange synonyms for your existing payees with those from transactions.


### Installation

**Run in console**
```
cd /<project_root>/
python3 -m venv <path_to_venv>
. /<path_to_venv>/bin/activate
pip install -r requirements.txt
cp ./example.env .env
```

**Fill .env with your credentials**
To get your YNAB access token follow the [instruction](https://api.youneedabudget.com/) "Quick Start" chapter.
Rest of YNAB's attributes you can get from the YNAB UI. They are part of URLs
```
https://app.youneedabudget.com/<BUDGET_ID>/accounts/<ACCOUNT_ID>
```


All transactions from `ABNA_IBAN_1` will be transfered at `YNAB_ACCOUNT_1`
From `ABNA_IBAN_2` to `YNAB_ACCOUNT_2` and so on. You can add as many account as you wish.
The only requirements:
1. indices should start from 1
2. do not skip any of indices, otherwise, next indices will be ignored

**To run the script manually use command**
```
python main.py
```

To run it periodically use the cron:
```
crontab -e
```
Add for example this line using your favorite editor:
```
0 9-22 * * * cd /<project_root>/; venv/bin/python ./random_start.py
```
This command will start the script every hour between 09:00 and 22:00 at random minute and second.

### Contribution
I am always happy to have any help with new features and bugfixes. Feel free to send pull requests.
