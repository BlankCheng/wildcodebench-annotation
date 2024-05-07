import numpy as np
import matplotlib.pyplot as plt


def f_446():
    """
    Creates and displays a diagram of a parabola represented by the equation y = x^2.
    The function plots the parabola using matplotlib, sets the title as 'y = x^2', labels the axes as 'x' and 'y',
    and enables the grid. It uses a fixed range for x values from -10 to 10 with 400 points.
    This function is used for demonstrating basic plotting capabilities and visualizing
    quadratic functions. The function does not take any parameters and does not return any value.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Parameters:
    None
    
    Returns:
    None
    
    Examples:
    >>> f_446() # This will display the plot of the parabola y = x^2
    >>> type(f_446())
    <class 'NoneType'>
    """
    X = np.linspace(-10, 10, 400)
    Y = X**2
    plt.figure()
    plt.plot(X, Y)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def test_no_error(self):
        """Test that the function runs without error."""
        try:
            f_446()
        except Exception as e:
            self.fail(f"Function f_446 raised an exception: {e}")
    def test_plot_elements(self):
        """Test that the plot contains correct elements like title and labels."""
        with patch('matplotlib.pyplot.show'):
            f_446()
            fig = plt.gcf()
            self.assertEqual(fig.axes[0].get_title(), 'y = x^2')
            self.assertEqual(fig.axes[0].get_xlabel(), 'x')
            self.assertEqual(fig.axes[0].get_ylabel(), 'y')
    @patch('numpy.linspace')
    @patch('matplotlib.pyplot.plot')
    def test_plot_data(self, mock_plot, mock_linspace):
        """Test if the plot contains the correct data."""
        mock_linspace.return_value = np.linspace(-10, 10, 400)
        expected_X = np.linspace(-10, 10, 400)
        expected_Y = expected_X ** 2
        with patch('matplotlib.pyplot.show'):
            f_446()
            mock_plot.assert_called_with(expected_X, expected_Y)
    def test_grid_enabled(self):
        """Test if the grid is enabled in the plot."""
        with patch('matplotlib.pyplot.show'):
            f_446()
            fig = plt.gcf()
            self.assertTrue(fig.axes[0].get_xgridlines()[0].get_visible())
            self.assertTrue(fig.axes[0].get_ygridlines()[0].get_visible())
    @patch('matplotlib.pyplot.show')
    def test_show_called(self, mock_show):
        """Test that plt.show() is called to display the plot."""
        f_446()
        mock_show.assert_called_once()
