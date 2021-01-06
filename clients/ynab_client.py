import json

import requests

import settings


class YnabClient:
    BASE_URL = "https://api.youneedabudget.com/v1"

    def _call(self, url, method="get", data=None):
        headers = {
            "Authorization": "Bearer {}".format(settings.YNAB_ACCESS_TOKEN),
            "Content-Type": "application/json"
        }
        if data:
            data = json.dumps(data)
        response = getattr(requests, method)(
            url=self.BASE_URL + url,
            data=data,
            headers=headers
        )
        print("{}: {}".format(response.status_code, response.content))
        response.raise_for_status()
        return response.json()['data']

    def get_budgets(self):
        """
        https://api.youneedabudget.com/v1#/Budgets/getBudgets
        :return:
        """
        return self._call('/budgets')

    def get_accounts(self):
        """
        https://api.youneedabudget.com/v1#/Accounts/getAccounts
        """
        return self._call("/budgets/{budget_id}/accounts".format(budget_id=settings.YNAB_BUDGET_ID))

    def get_payees(self):
        """
        https://api.youneedabudget.com/v1#/Payees/getPayees
        """
        return self._call("/budgets/{budget_id}/payees".format(budget_id=settings.YNAB_BUDGET_ID))

    def get_transactions(self):
        """
        https://api.youneedabudget.com/v1#/Transactions/getTransactions
        """
        return self._call("/budgets/{budget_id}/transactions".format(budget_id=settings.YNAB_BUDGET_ID))

    def add_transactions(self, data):
        """
        https://api.youneedabudget.com/v1#/Transactions/createTransaction
        """
        return self._call(
            "/budgets/{budget_id}/transactions".format(budget_id=settings.YNAB_BUDGET_ID),
            method="post",
            data=data
        )
