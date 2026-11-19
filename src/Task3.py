import numpy as np
import pandas as pd
marks = np.array([[70, 80, 90],
[60, 75, 85],
[88, 92, 79],
[55, 65, 70]])

print("shape: ", marks.shape)
print("Type :",type(marks))
print("Size :", len(marks))
print("Student Average : ",np.mean(marks, axis=1))
print("Subject Average : ",np.mean(marks, axis=0))
print("grace marks",marks+5)
weights = np.array([0.3, 0.3, 0.4])

weighted_scores = np.dot(marks, weights)

print("weighted score: ",weighted_scores)

df = pd.read_csv("Test1/employees.csv")
print(df)
print(df.info())
print(df.describe())
print (df.loc[0])
print(df.iloc[0:2])
print( "salary greater than 350000 :")
print(df[df["salary"]>35000])