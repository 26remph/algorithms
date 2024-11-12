import numpy as np
import pandas as pd

students = pd.read_csv('sample_ds.csv')

# adding calculate column
scores = students.assign(total_score=lambda x: (x['math score'] +
                                               x["reading score"] + x["writing score"])
                         )
print(scores.sort_values('total_score', ascending=False).head(10))

# group by example
print(students.groupby(['gender', 'test preparation course'])['writing score'].count())

# aggregate example
agg_function = {"math score": ['mean', 'median']}
print(students.groupby(['gender', "test preparation course"]).agg(agg_function))
