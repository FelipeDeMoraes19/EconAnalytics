import unittest
import pandas as pd
from src.data.process_data import load_data, clean_data

class TestDataProcessing(unittest.TestCase):

    def test_load_data(self):
        data = load_data('../../data/raw/gdp_data.csv')
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

    def test_clean_data(self):
        data = pd.read_csv('../../data/raw/gdp_data.csv')
        cleaned_data = clean_data(data)
        self.assertIsNotNone(cleaned_data)
        self.assertFalse(cleaned_data.empty)

if __name__ == '__main__':
    unittest.main()
