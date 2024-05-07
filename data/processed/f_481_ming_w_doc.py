import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def f_391(L):
    '''
    Convert a list of lists 'L' into a Pandas DataFrame filled with random integers, with the number of rows and columns corresponding to the integers in the nested lists.
    
    Requirements:
    - numpy
    - pandas

    Parameters:
    L (list of lists): A list of lists where each sublist contains two integers.
    
    Returns:
    DataFrame: A pandas DataFrame with random integers.
    
    Example:
    >>> df = f_391([[2, 3], [5, 6]])
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    '''
    rows, columns = L[0][0] * L[0][1], L[1][0] * L[1][1]
    random_array = np.random.randint(RANGE[0], RANGE[1], size=(rows, columns))
    df = pd.DataFrame(random_array)
    return df

import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = f_391([[2, 3], [5, 6]])
        self.assertEqual(result.shape, (2*3, 5*6))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_2(self):
        result = f_391([[1, 1], [1, 1]])
        self.assertEqual(result.shape, (1*1, 1*1))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_3(self):
        result = f_391([[4, 5], [2, 3]])
        self.assertEqual(result.shape, (4*5, 2*3))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_4(self):
        result = f_391([[3, 2], [6, 5]])
        self.assertEqual(result.shape, (3*2, 6*5))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_5(self):
        result = f_391([[7, 8], [1, 2]])
        self.assertEqual(result.shape, (7*8, 1*2))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
