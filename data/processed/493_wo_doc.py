from datetime import datetime
import random
import matplotlib.pyplot as plt


def task_func(
    epoch_milliseconds,
    teams=["Team1", "Team2", "Team3", "Team4", "Team5"],
    random_seed=0,
):
    """
    Generate and plot a performance trend for different teams from a given epoch timestamp to the current time.

    The performance data is generated by creating a series of random values for each day from the starting timestamp
    to the present day. Each team's performance is simulated as a random float between 0.1 and 1 for each day.
    The plot shows days since the start date on the x-axis and performance on the y-axis.

    Parameters:
    epoch_milliseconds (int): The epoch milliseconds from where to start the generation. Must not be in the future.
    teams (list of str, optional): Team names. If not provided, defaults to ['Team1', 'Team2', 'Team3', 'Team4', 'Team5'].
    random_seed (int, optional): Seed for random number generation to ensure reproducibility. Defaults to 0.

    Returns:
    dict: A dictionary containing performance data for each team, with days as indices and performance as float values.
    matplotlib.figure.Figure: A figure object showing the performance trend of each team over the days.

    Requirements:
    - datetime.datetime
    - random
    - matplotlib

    Example:
    >>> results, ax = task_func(1236472051807)
    >>> results.keys()
    dict_keys(['Team1', 'Team2', 'Team3', 'Team4', 'Team5'])
    >>> type(ax)
    <class 'matplotlib.figure.Figure'>
    """
    random.seed(random_seed)
    if (not isinstance(teams, list)) or (not all(isinstance(t, str) for t in teams)):
        raise TypeError("Expected teams to be list of str")
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    current_time = datetime.now()
    days_diff = (current_time - start_time).days
    if days_diff < 0:
        raise ValueError("Input epoch timestamp is in the future!")
    performance_data = {team: [0] * days_diff for team in teams}
    for i in range(days_diff):
        for team in teams:
            performance = random.uniform(0.1, 1)
            performance_data[team][i] += performance
    fig, ax = plt.subplots()
    for team, performance in performance_data.items():
        ax.plot(range(days_diff), performance, label=team)
    ax.set_xlabel("Days since " + start_time.strftime("%Y-%m-%d %H:%M:%S"))
    ax.set_ylabel("Performance")
    ax.legend()
    return performance_data, fig

import unittest
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.x = 1631295600000
        self.default_valid_teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    def _check_valid_performance_data(self, performance_data, valid_teams):
        self.assertIsInstance(performance_data, dict)
        self.assertTrue(all(team in valid_teams for team in performance_data.keys()))
        for team, performances in performance_data.items():
            for performance in performances:
                self.assertTrue(
                    0.1 <= performance <= 1, f"Performance out of range for {team}"
                )
                self.assertIsInstance(performance, float)
    def _check_plot(self, fig):
        ax = fig.axes[0]
        self.assertIsInstance(fig, plt.Figure)
        self.assertEqual(ax.get_ylabel(), "Performance")
        self.assertTrue(ax.get_xlabel().startswith("Days since"))
    def test_case_1(self):
        # Test basic case with default parameters - data
        performance_data, _ = task_func(self.x)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)
    def test_case_2(self):
        # Test basic case with default parameters - plot
        _, fig = task_func(self.x)
        self._check_plot(fig)
    def test_case_3(self):
        # Test basic case with custom input
        performance_data, fig = task_func(1236472051807, random_seed=42)
        self._check_plot(fig)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)
    def test_case_4(self):
        # Test custom parameters - custom teams
        for custom_teams in [["A", "B"], ["c d e", "F", "GH", "ij kl"]]:
            performance_data, fig = task_func(self.x, teams=custom_teams, random_seed=42)
            self._check_plot(fig)
            self._check_valid_performance_data(performance_data, custom_teams)
    def test_case_5(self):
        # Test custom parameters - random seed
        performance_data1, _ = task_func(self.x, random_seed=42)
        performance_data2, _ = task_func(self.x, random_seed=42)
        performance_data3, _ = task_func(self.x, random_seed=0)
        self.assertEqual(performance_data1, performance_data2)
        self.assertNotEqual(performance_data1, performance_data3)
    def test_case_6(self):
        # Test error handling for invalid input time
        future_epoch = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(future_epoch)
    def test_case_7(self):
        # Test error handling for invalid team
        with self.assertRaises(TypeError):
            task_func(self.x, [1, 2, 3])
        with self.assertRaises(TypeError):
            task_func(self.x, [[]])
    def tearDown(self):
        plt.close("all")
