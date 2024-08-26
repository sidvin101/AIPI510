import unittest
import pandas as pd
from medal_search import get_medal_counts

class TestMedalCounts(unittest.TestCase):

    def test_invalid_country(self):
        true_state = """
I'm sorry, either this country does not exist or have not participated in this
year's Olympics. If you believe that this is not the case, please check your
spelling. The full name of the country or the abbreviation are enough.
"""
        self.assertEqual(get_medal_counts("United Gates"), true_state)

    def test_valid_country(self):
        true_state = "UNITED STATES has 40 Gold medals, 44 Silver medals, and 42 Bronze medals. A total of 126 medals."

        self.assertEqual(get_medal_counts("United States"), true_state)

    def test_valid_country2(self):
        true_state = "CHINA has 40 Gold medals, 27 Silver medals, and 24 Bronze medals. A total of 91 medals."

        self.assertEqual(get_medal_counts("China"), true_state)

    def test_valid_country_lower(self):
        true_state = "UNITED STATES has 40 Gold medals, 44 Silver medals, and 42 Bronze medals. A total of 126 medals."

        self.assertEqual(get_medal_counts("united states"), true_state)

    def test_valid_country_abbr(self):
        true_state = "UNITED STATES has 40 Gold medals, 44 Silver medals, and 42 Bronze medals. A total of 126 medals."

        self.assertEqual(get_medal_counts("us"), true_state)
