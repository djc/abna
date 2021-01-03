from datetime import datetime

import settings
from clients.abn_client import ABNClient
from clients.ynab_client import YnabClient


class Abna2Ynab:
    abn_client = None

    def run(self):
        mutations = self.get_mutations()
        transactions = self.mutations2transactions(mutations)
        self.save_transactions(transactions)
        self.abn_client.save_last_transaction_timestamp()

    def get_mutations(self):
        print("ABN AMRO Authentication")
        self.abn_client = ABNClient()
        print("Get ABN AMRO mutations")
        self.abn_client.get_mutations()
        return self.abn_client.mutations

    def mutations2transactions(self, mutations):
        print("Convert abn amro mutations to ynab transactions")
        result = []
        for m in mutations:
            d = {
                "account_id": settings.YNAB_ACCOUNT_ID,
                "date": str(datetime.strptime(m['transactionTimestamp'], "%Y%m%d%H%M%S%f").date()),
                "amount": int(m['amount'] * 1000),
                "payee_name": m['counterAccountName'],
                "memo": " ".join(l.strip() for l in m['descriptionLines'])[:200],
                "import_id": "ABNAMRO:{}".format(m['transactionTimestamp'])
            }
            result.append(d)
        print("{} transactions ready to be added".format(len(result)))
        return {"transactions": result}

    def save_transactions(self, transactions):
        print("Save transactions to YNAB")
        ynab = YnabClient()
        ynab.add_transactions(transactions)


if __name__ == '__main__':
    obj = Abna2Ynab()
    obj.run()
