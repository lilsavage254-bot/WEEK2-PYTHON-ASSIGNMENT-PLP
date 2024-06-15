import unittest

# A class for the bank account.
class BankAccount:
    def __init__(self, initial_balance):        # Constructor for the BankAccount class
        self.balance = initial_balance          # Initial balance of the account

    def deposit(self, amount):                  # Method to deposit money into the account
        self.balance += amount                  # Add the amount to the balance
        return True                             # Return True if the deposit is successful

    def withdraw(self, amount):                 # Method to withdraw money from the account
        if self.balance >= amount:              # Check if the balance is greater than the amount to be withdrawn
            self.balance -= amount              # Subtract the amount from the balance
            return True                         # Return True if the withdrawal is successful
        return False                            # Return False if the withdrawal is unsuccessful

# Test case for the BankAccount class
class TestBankOperations(unittest.TestCase):    # Test case class for the BankAccount class
    def test_deposit(self):                     # Test method for the deposit method
        account = BankAccount(100)              # Create an instance of the BankAccount class with an initial balance of 100
        self.assertTrue(account.deposit(50))      # This will pass
        self.assertEqual(account.balance, 150)    # This will pass
    
    def test_withdraw(self):                    # Test method for the withdraw method
        account = BankAccount(100)              # Create an instance of the BankAccount class with an initial balance of 100
        self.assertTrue(account.withdraw(50))     # This will pass
        self.assertEqual(account.balance, 50)     # This will pass
    
    def test_overdraft(self):                     # Test method for the withdraw method
        account = BankAccount(100)                # This will pass
        self.assertFalse(account.withdraw(200))   # This will pass
        self.assertEqual(account.balance, 100)    # This will pass


if __name__ == "__main__" :                       # This will pass
    unittest.main()                               # This will pass

