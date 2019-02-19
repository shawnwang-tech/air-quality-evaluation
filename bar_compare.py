import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

df=pd.read_csv("whole_prediction.csv")

#
# fig = plt.figure(figsize=(20, 10))
#
#
# ax = fig.add_subplot(121)
# tmp=df[df["test_set"]=="PPA"]
# ax=sns.barplot(x="smoothing_window(hour)", y="RMSE", hue="weather_data_used", data=tmp, ax=ax )
# ax.set_title("PPA data")
#
# ax = fig.add_subplot(122)
# tmp=df[df["test_set"]=="EPA"]
# ax=sns.barplot(x="smoothing_window(hour)", y="RMSE", hue="weather_data_used", data=tmp, ax=ax )
# ax.set_title("EPA data")
#
# plt.show()

fig = plt.figure(figsize=(20, 10))


ax = fig.add_subplot(121)
tmp=df[df["weather_data_used"]==True]
ax=sns.barplot(x="smoothing_window(hour)", y="RMSE", hue="test_set", data=tmp, ax=ax )
ax.set_title("with weather data")

ax = fig.add_subplot(122)
tmp=df[df["weather_data_used"]==False]
ax=sns.barplot(x="smoothing_window(hour)", y="RMSE", hue="test_set", data=tmp, ax=ax )
ax.set_title("no weather data")

plt.show()