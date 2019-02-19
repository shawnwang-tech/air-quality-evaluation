import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("monthly_prediction_evaluation.csv",  parse_dates=["timestamp"], infer_datetime_format=True)
sns.set(style="whitegrid")

fig = plt.figure(figsize=(20, 10))



# ax.set_title("montly prediction")
# sns.lineplot(x="timestamp", y="RMSE", hue="abbr", data=df, ax=ax)

# smoothing window

ax = fig.add_subplot(211)
ax.set_title("PPA data")
tmp=df[(df["weather_data_used"]==False) & (df["test_set"]=="PPA")]
sns.lineplot(x="timestamp", y="RMSE", hue="smoothing_window(hour)", data=tmp, ax=ax, legend="full")

ax=fig.add_subplot(212)
ax.set_title("EPA data")
tmp=df[ (df["weather_data_used"]==False) & (df["test_set"]=="EPA")]
sns.lineplot(x="timestamp", y="RMSE", hue="smoothing_window(hour)", data=tmp, ax=ax, legend="full")

plt.show()

#weather data

# ax = fig.add_subplot(211)
# ax.set_title("PPA data")
# tmp=df[ (df["test_set"]=="PPA")]
# sns.lineplot(x="timestamp", y="RMSE", style="weather_data_used", hue="smoothing_window(hour)", legend="full", data=tmp, ax=ax, ci=None)
#
# ax=fig.add_subplot(212)
# ax.set_title("EPA data")
# tmp=df[ (df["test_set"]=="EPA")]
# sns.lineplot(x="timestamp", y="RMSE", style="weather_data_used", hue="smoothing_window(hour)", legend="full",  data=tmp, ax=ax, ci=None)
#
# plt.show()

# PPA vs EPA
# ax = fig.add_subplot(211)
# ax.set_title("with weather data")
# tmp=df[ (df["weather_data_used"]==True)]
# sns.lineplot(x="timestamp", y="RMSE", style="test_set", hue="smoothing_window(hour)", legend="full", data=tmp, ax=ax)
#
# ax = fig.add_subplot(212)
# ax.set_title("no weather data")
# tmp=df[ (df["weather_data_used"]==False)]
# sns.lineplot(x="timestamp", y="RMSE", style="test_set", hue="smoothing_window(hour)", legend="full", data=tmp, ax=ax)
#
# plt.show()