class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            print('The amount is negative')

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughBalanceException("You don't have enough Balance. Your Current Balance is " + str(self._balance))
        if amount <= 0:
            raise NegativeAmountException("The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount is: " + str(amount))
            print("New Balance updated as: " + str(self._balance))

    def get_balance(self):
        print("Current balance is: " + str(self._balance))
        return self._balance

    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.01
    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

class CheckingAccount(Account):
    pass

class BankException(Exception):
    pass

class NegativeAmountException(BankException):
    pass

class NotEnoughBalanceException(BankException):
    pass

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    # Customer Factory
    def new_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        #TODO add customer to a list
        self.customers.append(c)
        return c

    # Add account factory to bank
    def new_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    # Implement transfer
    def transfer(self, from_acc_id, to_acc_id, amount):
        #TODO implement
        if from_acc_id not in self.accounts:
            print("The sender account id you input doesn't exist")
            return

        if amount <= 0:
            print("The transfer amount is negative. Please input the positive amount")
            return

        balance_from_acc_id = from_acc_id.get_balance()
        if amount > balance_from_acc_id:
            print("You don't have enough Balance in your account to transfer this amount")
            return

        else:
            print("Your transfer is successful")
            from_acc_id.charge(amount)
            to_acc_id.deposit(amount)

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customers, self.accounts)

bank = Bank()
bank_2 = Bank()

c1 = bank.new_customer('John', 'Smith')
print(c1)
c2 = bank.new_customer('Anne', 'Brown')
print(c2)

a1 = bank.new_account(c1)
print(a1)
a2 = bank.new_account(c2)
print(a2)
a3 = bank_2.new_account(c2)

a1.deposit(300)
a2.deposit(20)
a3.deposit(500)

# Transferred well case
bank.transfer(a1,a2,50)
a1.get_balance()
a2.get_balance()
print() # a1, a2 customer's balance changed

# Exception case (NotEnoughBalanceTransferException)
bank.transfer(a1,a2,500)
a1.get_balance()
a2.get_balance()
print() # a1, a2 customer's balance didn't change due to exceptional case

# Exception case (NegativeAmountTransferException)
bank.transfer(a1,a2,-100)
a1.get_balance()
a2.get_balance()
print() # a1, a2 customer's balance didn't change due to exceptional case

# Exception case (AccountIDNotAvailable)
bank.transfer(a3,a2,60)
a3.get_balance()
a2.get_balance()
print() # a3, a2 customer's the balance didn't change due to exceptional case