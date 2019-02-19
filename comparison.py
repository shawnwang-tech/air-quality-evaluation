import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# dirs = {
#     'utah_1711_1806_validation_ppa_epa_pm25_w_6hr': "epa weather 6hr",
#         'utah_1711_1806_validation_ppa_epa_pm25_6hr':"epa 6hr",
#         'utah_1711_1806_validation_ppa_ppa_pm25_6hr': "ppa 6hr",
#         'utah_1711_1806_validation_ppa_ppa_pm25_w_6hr':"ppa weather 6hr"
# }

def compare_parameter_bar(paths, date_range, metric, filename=None):
    dfs = []
    for p in paths:
        months = os.listdir(p)
        months = list(
            filter(lambda x: not (x.startswith(".") or x.endswith(".txt") or x.endswith(".png") or x.endswith(".csv")),
                   months))
        months.sort()
        # month -> dir name of every month
        i=0
        for month in months:
            eval_result_month = os.path.join(p, month+".txt")
            with open(eval_result_month, "r") as f:
                evaluation_result=eval(f.read())
            evaluation_result = {k:[evaluation_result[k]] for k in evaluation_result}
            df=pd.DataFrame.from_dict(evaluation_result)
            df["period"]=date_range[i]
            df["cat"]=paths[p]
            dfs.append(df)
            i+=1
    result = pd.concat(dfs)

    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    sns.set(style="whitegrid")
    # ax=sns.barplot(x="period", y=metric, hue="cat", data=result, ax=ax)
    ax = sns.lineplot(x="period", y=metric, hue="cat", data=result, ax=ax)
    plt.show()

working_dir = os.getcwd()
dirs = {
        'utah_1711_1806_validation_ppa_epa_pm25_w_1hr': "epa weather 1hr",
            'utah_1711_1806_validation_ppa_epa_pm25_1hr':"epa 1hr",
            'utah_1711_1806_validation_ppa_ppa_pm25_1hr': "ppa 1hr",
            'utah_1711_1806_validation_ppa_ppa_pm25_w_1hr':"ppa weather 1hr"
}
paths= { os.path.join(working_dir, k) :v  for k,v in dirs.items()}
date_range=pd.period_range(start='2017-11-01', end='2018-05-01', freq='M')

compare_parameter_bar(paths, date_range, "RMSE", "1 hour comparison.png")