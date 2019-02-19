import os
import pandas as pd
import re

# dirs = [
#     #  'utah_1711_180601_validation_ppa_epa_pm25_w',
#         'utah_1711_1806_validation_ppa_epa_pm25_12hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_1hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_24hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_6hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_w_12hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_w_1hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_w_24hr',
#         'utah_1711_1806_validation_ppa_epa_pm25_w_6hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_12hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_1hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_24hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_6hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_w_12hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_w_1hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_w_24hr',
#         'utah_1711_1806_validation_ppa_ppa_pm25_w_6hr']
#
# paths=list( map(lambda x: os.path.join(os.getcwd(), x+".txt") , dirs))
#
# dfs=[]
# for p in paths:
#     with open(p, "r") as f:
#         evaluation_result = eval(f.read())
#     evaluation_result = {k: [evaluation_result[k]] for k in evaluation_result}
#     df=pd.DataFrame.from_dict(evaluation_result)
#     file_name=os.path.basename(p)
#     df["name"]= file_name
#     print(file_name)
#     df["test_set"]= "EPA" if "ppa_epa" in file_name else "PPA"
#     df["smoothing_window(hour)"]= int( re.search("[0-9]+hr", file_name).group(0)[:-2])
#     df["weather_data_used"]= True if "_w" in file_name else False
#     df["abbr"]=" ".join([
#         "EPA" if "ppa_epa" in file_name else "PPA",
#         re.search("[0-9]+hr", file_name).group(0),
#         "w" if "_w" in file_name else ""
#     ])
#     dfs.append(df)
# df=pd.concat(dfs)
# df.to_csv("whole_prediction.csv")


dirs = [
    #  'utah_1711_180601_validation_ppa_epa_pm25_w',
    'utah_1711_1806_validation_ppa_epa_pm25_12hr',
    'utah_1711_1806_validation_ppa_epa_pm25_1hr',
    'utah_1711_1806_validation_ppa_epa_pm25_24hr',
    'utah_1711_1806_validation_ppa_epa_pm25_6hr',
    'utah_1711_1806_validation_ppa_epa_pm25_w_12hr',
    'utah_1711_1806_validation_ppa_epa_pm25_w_1hr',
    'utah_1711_1806_validation_ppa_epa_pm25_w_24hr',
    'utah_1711_1806_validation_ppa_epa_pm25_w_6hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_12hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_1hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_24hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_6hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_w_12hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_w_1hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_w_24hr',
    'utah_1711_1806_validation_ppa_ppa_pm25_w_6hr']

paths = list(map(lambda x: os.path.join(os.getcwd(), x), dirs))
date_range=pd.period_range(start='2017-11-01', end='2018-05-01', freq='M')


dfs = []
for p in paths:
    file_name = os.path.basename(p)
    test_set = "EPA" if "ppa_epa" in file_name else "PPA"
    smoothing_window = int(re.search("[0-9]+hr", file_name).group(0)[:-2])
    weather = True if "_w" in file_name else False
    abbr = " ".join([
        test_set,
        str(smoothing_window),
        "w" if "_w" in file_name else ""
    ])

    months = os.listdir(p)
    months = list(filter(lambda x: x.endswith(".txt"), months) )
    months.sort()
    i = 0
    for month in months:
        with open(os.path.join(p, month), "r") as f:
            evaluation_result = eval(f.read())
        evaluation_result = {k: [evaluation_result[k]] for k in evaluation_result}
        df = pd.DataFrame.from_dict(evaluation_result)
        df["test_set"] = test_set
        df["smoothing_window(hour)"] = smoothing_window
        df["weather_data_used"] = weather
        df["abbr"] = abbr
        df["timestamp"]=date_range[i]
        dfs.append(df)
        i+=1
df = pd.concat(dfs)
df.set_index(keys="timestamp")
df.to_csv("monthly_prediction_evaluation.csv")
