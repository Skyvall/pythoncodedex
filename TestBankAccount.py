import unittest
from bank_account import BankAccount





class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)
        
    def tearDown(self):
        self.account = None
        
        
    def test_initial_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.balance, 100)
        
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
        
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)
        
if __name__ == "__main__":
    unittest.main()
    
