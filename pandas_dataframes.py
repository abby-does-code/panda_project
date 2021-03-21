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
Test 3     70   90   90     82

print(grades["Eva"])  # Column name

print(grades.Sam)  # Another valid identifier

# Loc and iloc methods
print(grades.loc["Test 2"])  # Referring to the names of the row

print(grades.iloc[1])  # i represents the integer indices

# For consecutive rows:
print
print(grades.iloc[0:2])

# for non-consecutive rows
print(grades.loc["Test 1", "Test 3"])
print(grades.iloc[[0, 3]])"""

# How do we view Eva and Katie's grades for test 1 and test 2?
##rows always go first

print(grades.loc[:"Test 2", ["Eva", "Katie"]])

print(grades.loc[["Test 1", "Test 3"], "Sam":"Katie"])

grade_90 = grades[grades >= 90]

print(grade_90)  # Nan = "Not a number"

####Create a dataframe for everyone with a B grade####
grades_B = [(grades >= 80) & (grades < 90)]

print(grades_B)

###Create a dataframe for everyone with a B or A###
grades_A_or_B = [(grades >= 90) | (grades >= 80)]

print(grades_A_or_B)

print(grades.describe())  # Stats by each column

pd.set_option("precision", 2)
print(grades.describe())

# by test
print(grades.T.describe())