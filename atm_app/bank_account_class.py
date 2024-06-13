from atm_app.account_class import Account


class BankAccount:
    def __init__(self):
        self.no_of_customers = 0
        self.accounts = []

    def add_account(self, name, pin):
        account_instance = Account(name, pin, self.generate_acct_no())
        self.accounts.append(account_instance)
        self.no_of_customers += 1

    def get_no_of_customers(self):
        return self.no_of_customers

    def generate_acct_no(self):
        self.get_no_of_customers() + 1

    def bank_deposit(self, acct_no, amount):

    def check_bank_balance(self, acct_no):


    def find_account(self, acct_no):
        for account in self.accounts:
            if account.get_account_number() == acct_no:
                return account
        return None
