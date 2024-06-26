import pandas as pd

df = pd.read_csv(r"C:\Users\vjmoo\FF App\.venv\test_cel.csv")
dataFrame = pd.DataFrame(df)
#gb = df.groupby('u_role')
dataFrame.insert(2, "Age", [21,22,45,34,22,22,34,36,29], True)
new =dataFrame.groupby(['Age', 'u_role'])['Age'].count()
print(new)
# sorting data frame by name
#dataFrame.sort_values("u_role", axis=0, ascending=True,
#                 inplace=True, na_position='last')

# saving the dataframe
#dataFrame.to_csv('pandas_cel.csv')