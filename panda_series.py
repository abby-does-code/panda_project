import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))

a = grades[0]
grades.count()
grades.mean()
grades.min(0)
grades.max()
grades.std()


grades.describe()

grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])
print(grades)


grades.Wally

grades.dtype
#dtype('int64')

grades.values
#Array([87,100,94])

