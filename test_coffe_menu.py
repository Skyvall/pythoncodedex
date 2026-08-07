import unittest
from cofee_menu import CofeeMenu


class TestCofeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CofeeMenu()
        
    def tearDown(self):
        self.menu = None

    def test_menu_prices(self):
        self.assertEqual(self.menu.prices['espresso'], 2.50)
        self.assertEqual(self.menu.prices['latte'], 3.50)
        self.assertEqual(self.menu.prices['cappuccino'], 3.00)
        self.assertEqual(self.menu.prices['americano'], 2.00)
        
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.prices.get('latte'), 3.50)
        
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.prices.get('mocha'))
        
        
if __name__ == "__main__":
    unittest.main()