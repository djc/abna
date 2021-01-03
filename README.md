# ABN2YNAB

This script is made to add your transactions from ABN AMRO to YNAB application

### Installation
```
cd /<project_root>/
python3 -m venv <path_to_venv>
. /<path_to_venv>/bin/activate
pip install -r requirements.txt
cp ./example.env .env
```

Fill your .env with your credentials

To get your YNAB access token follow the [instruction](https://api.youneedabudget.com/) "Quick Start" chapter.
Rest of YNAB's attributes you can get from the YNAP UI. They are part of URL

Add cronjob. For example:
```
0 9-22 * * * /<project_root>/venv/bin/python /<project_root>/random_start.py
```
This command will start the script every hour between 09:00 and 22:00 at random minute


### TODO
* Support multiple accounts
