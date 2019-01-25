from zzz_others.evaluation import get_rmse_mae_mape, get_sum_of_difference, get_me
import pandas as pd
import matplotlib.pyplot as plt


def error_analysis(file_name, date_name="timestamp", prediction_name="prediction_value", ground_truth_name="ground_truth", sensor_name="location"):
    df=pd.read_csv(file_name, parse_dates=[date_name], infer_datetime_format=True)
    df.set_index(date_name, inplace=True)
    rmse, mae, mape= get_rmse_mae_mape(df, ground_truth_name, prediction_name)
    print("rmse %s"%(rmse))
    print("mae %s"%(mae))
    print("mape %s"%(mape))
    sum_diff=get_sum_of_difference(df, ground_truth_name, prediction_name)
    print("sum of difference %s"%(sum_diff))
    avg_diff=get_me(df, ground_truth_name, prediction_name)
    print("me %s"%(avg_diff))
    sensors=df.groupby([sensor_name])
    i=0
    for sensor_id in sensors.groups.keys():
        node = sensors.get_group(sensor_id)
        ax=plt.subplot(len(sensors.groups.keys()), 1, 1+i)
        node[[ground_truth_name, prediction_name]].plot( title="node:" + str(sensor_id), ax=ax)
        i += 1
    plt.show()

if __name__ == '__main__':
    #error_analysis("../utah_171101_180101_validation_ppa_ppa_pm25_6_0.01/prediction.csv")
    error_analysis("../utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction.csv")

