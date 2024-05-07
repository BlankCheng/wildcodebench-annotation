from dateutil.parser import parse
from datetime import timedelta


def f_32(date_str):
    """
    Get the next business day (Mon-Fri) after a certain date string.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd" format.

    Returns:
    datetime: The datetime object of the next business day.

    Requirements:
    - datetime
    - dateutil.parser

    Example:
    >>> f_32('2022-10-22')
    datetime.datetime(2022, 10, 24, 0, 0)
    >>> f_32('2022-10-28')
    datetime.datetime(2022, 10, 31, 0, 0)
    """
    given_date = parse(date_str)
    next_day = given_date
    while True:
        next_day = next_day + timedelta(days=1)
        if 0 <= next_day.weekday() < 5:
            break
    return next_day

import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = f_32('2022-10-22')
        self.assertEqual(result, datetime(2022, 10, 24, 0, 0))
    
    def test_case_2(self):
        result = f_32('2022-10-28')
        self.assertEqual(result, datetime(2022, 10, 31, 0, 0))
    
    def test_case_3(self):
        result = f_32('2022-10-30')
        self.assertEqual(result, datetime(2022, 10, 31, 0, 0))
    
    def test_case_4(self):
        result = f_32('2022-10-31')
        self.assertEqual(result, datetime(2022, 11, 1, 0, 0))
    
    def test_case_5(self):
        result = f_32('2022-11-02')
        self.assertEqual(result, datetime(2022, 11, 3, 0, 0))
