import pandas as pd
from scipy import stats



def f_235(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.
    
    Parameters:
    matrix (array): The 2D numpy array.
    
    Returns:
    DataFrame: The normalized DataFrame.

    Requirements:
    - pandas
    - numpy
    - scipy

    Example:
    >>> import numpy as np
    >>> matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> normalized_df = f_235(matrix)
    >>> isinstance(normalized_df, pd.DataFrame)
    True
    >>> np.allclose(normalized_df.mean(), 0)
    True
    >>> np.allclose(normalized_df.std(ddof=0), 1)
    True
    """
    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = f_235(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745],
            2: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_2(self):
        matrix = np.array([[2, 5], [5, 2]])
        result = f_235(matrix)
        expected_result = pd.DataFrame({
            0: [-1.0, 1.0],
            1: [1.0, -1.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_3(self):
        matrix = np.array([[5]])
        result = f_235(matrix)
        expected_result = pd.DataFrame({
            0: [0.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_4(self):
        matrix = np.array([[1, 3], [2, 4], [3, 5]])
        result = f_235(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_5(self):
        matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
        result = f_235(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745],
            2: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)
