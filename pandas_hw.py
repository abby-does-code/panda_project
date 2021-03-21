# START#
"""Perform the following tasks with pandas Series:"""

import pandas as pd
import numpy as np

"""Create a Series from the list [7, 11, 13, 17]."""
the_list = [7, 11, 13, 17]
list_series = pd.Series(the_list)

"""Create a Series with five elements that are all 100.0."""

series1 = [100 for i in range(20)]
same_num_series = pd.Series(series1)
print(same_num_series)

"""Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use method describe to produce the Series’ basic descriptive statistics."""

random_series_data = np.random.randint(0, 101, size=20)

random_series = pd.Series([random_series_data])

print(random_series.describe())

"""Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'."""

temp_series = pd.Series(
    [98.6, 98.9, 100.2, 97.9], index=["Julie", "Charlie", "Sam", "Andrea"]
)
print(temp_series)

"""Form a dictionary from the names and values in Part (4), then use it to initialize a Series."""

names_dict = dict(Julie=98.6, Charlie=98.9, Sam=100.2, Andrea=97.9)

series_from_dict = pd.Series(names_dict)
print(series_from_dict)