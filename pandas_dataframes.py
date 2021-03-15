# Taking a dictionary and turning it into a dataframe
##Enahnced two dimensional array
##Custom indexes for rows and columns
##Additional capabilities; supports missing data
##Each column in a dataframe is a one-dimensional series

import pandas as pd

grades_dict = dict(
    Wally=[87, 96, 70], Eva=[100, 87, 90], Sam=[94, 77, 90], Katie=[100, 81, 82]
)

grades = pd.DataFrame(grades_dict)

grades.index = ["Test 1", "Test 2", "Test 3"]
"""print(grades)
        Wally  Eva  Sam  Katie
Test 1     87  100   94    100
Test 2     96   87   77     81
Test 3     70   90   90     82"""

print(grades["Eva"])  # Column name

print(grades.Sam)  # Another valid identifier

# Loc and iloc methods
print(grades.loc["Test 2"]) #Referring to the names of the column

print(grades.iloc[1]) #i represents the integer indices 