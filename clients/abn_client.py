import abna

import settings


class ABNClient:
    mutations = None
    new_last_transaction_timestamp = None
    FILENAME = "last_transaction_timestamp.txt"

    def get_mutations(self):
        sess = abna.Session(settings.ABNA_ACCOUNT)
        sess.login(settings.ABNA_PASSNUMBER, settings.ABNA_PASSWORD)
        mutations = sess.mutations(settings.ABNA_ACCOUNT)
        self.mutations = self.get_only_new_mutations(mutations)

    def get_only_new_mutations(self, mutations):
        result = []
        last_transaction_timestamp = self.get_last_transaction_timestamp()
        for mutation in mutations['mutationsList']['mutations']:
            transaction_timestamp = int(mutation['mutation']['transactionTimestamp'])
            if not self.new_last_transaction_timestamp or transaction_timestamp > self.new_last_transaction_timestamp:
                self.new_last_transaction_timestamp = transaction_timestamp
            if transaction_timestamp > last_transaction_timestamp:
                result.append(mutation['mutation'])
        return result

    def save_last_transaction_timestamp(self):
        with open(self.FILENAME, 'w') as f:
            f.write(str(self.new_last_transaction_timestamp))

    def get_last_transaction_timestamp(self):
        with open(self.FILENAME, 'r') as f:
            return int(f.readline())
