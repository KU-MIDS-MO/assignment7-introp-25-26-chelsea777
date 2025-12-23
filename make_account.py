def make_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        if amount<=0:
            raise ValueError
        if amount >balance:
            raise ValueError
        balance -=amount
        return balance
    return deposit, withdraw
  