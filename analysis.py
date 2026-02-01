import pandas as pd

df = pd.read_csv("burnout.csv")

df.head()
df.info()
df.describe()

df.isnull().sum()
df = df.dropna()


df.shape

res =df["burnout_risk"].value_counts()
res1 = df.groupby("work_hours")["burnout_score"].mean()
res2 = df[df["work_hours"] > 9]
res3 = df.groupby("sleep_hours")["burnout_score"].mean()
res4 = df.groupby("screen_time_hours")["burnout_score"].mean()
res5 = df.groupby("burnout_risk")["burnout_score"].mean()
res6 = df.groupby("task_completion_rate")["burnout_score"].mean()


print(res)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)

import matplotlib.pyplot as plt

df["burnout_score"].hist()
plt.title("Burnout Score Distribution")
plt.show()

df.boxplot(column="burnout_score", by="burnout_risk")
plt.show()
