import abna
import json
import settings


class ABNClient:
    mutations = None
    new_last_transaction = None
    FILENAME = "last_transactions.json"

    def __init__(self):
        self.sess = abna.Session(settings.ABNA_ACCOUNT)
        self.sess.login(settings.ABNA_PASSNUMBER, settings.ABNA_PASSWORD)
        self.last_transactions = self.get_last_transaction_timestamp()

    def get_mutations(self, iban):
        mutations = self.sess.mutations(iban)
        return self.get_only_new_mutations(iban, mutations)

    def get_only_new_mutations(self, iban, mutations):
        result = []
        last_transaction_timestamp = int(self.last_transactions.get(iban, 0))
        new_last_transaction = 0
        for mutation in mutations['mutationsList']['mutations']:
            transaction_timestamp = int(mutation['mutation']['transactionTimestamp'])
            if transaction_timestamp > new_last_transaction:
                new_last_transaction = transaction_timestamp
            if transaction_timestamp > last_transaction_timestamp:
                result.append(mutation['mutation'])
        self.last_transactions[iban] = new_last_transaction
        return result

    def save_last_transaction_timestamp(self):
        with open(self.FILENAME, 'w') as f:
            json.dump(self.last_transactions, f)

    def get_last_transaction_timestamp(self):
        try:
            with open(self.FILENAME, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}
