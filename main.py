from datetime import datetime

import settings
from clients.abn_client import ABNClient
from clients.ynab_client import YnabClient


class Abna2Ynab:
    abn_client = None

    def run(self):
        print("ABN AMRO Authentication")
        self.abn_client = ABNClient()
        for iban, account in settings.ACCOUNTS.items():
            print("######## {} : {} ########".format(iban, account))
            mutations = self.get_mutations(iban)
            if mutations:
                transactions = self.mutations2transactions(account, mutations)
                self.save_transactions({"transactions": transactions})
            else:
                print("There are no new transactions")
        self.abn_client.save_last_transaction_timestamp()

    def get_mutations(self, iban):
        print("Get ABN AMRO mutations")
        return self.abn_client.get_mutations(iban)

    def mutations2transactions(self, account, mutations):
        print("Convert abn amro mutations to ynab transactions")
        result = []
        for m in mutations:
            d = {
                "account_id": account,
                "date": str(datetime.strptime(m['transactionTimestamp'], "%Y%m%d%H%M%S%f").date()),
                "amount": int(m['amount'] * 1000),  # 1 euro equal to 1000 units
                "payee_name": m['counterAccountName'],
                "memo": " ".join(l.strip() for l in m['descriptionLines'])[:200],
                "import_id": "ABNAMRO:{}".format(m['transactionTimestamp'])
            }
            result.append(d)
        print("{} transactions ready to be added".format(len(result)))
        return result

    def save_transactions(self, transactions):
        print("Save transactions to YNAB")
        YnabClient().add_transactions(transactions)


if __name__ == '__main__':
    obj = Abna2Ynab()
    obj.run()
