# START#
"""Perform the following tasks with pandas Series:"""

import pandas as pd
import numpy as np

"""Create a Series from the list [7, 11, 13, 17]."""


"""Create a Series with five elements that are all 100.0."""

series1 = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])


"""Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use method describe to produce the Series’ basic descriptive statistics."""

random_series_data = np.random.randint(0, 101, size=20)

random_series = pd.Series([random_series_data])

print(random_series.describe())

"""Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
Form a dictionary from the names and values in Part (4), then use it to initialize a Series."""
