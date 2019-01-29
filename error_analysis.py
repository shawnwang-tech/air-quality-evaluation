from evaluation import get_all_metrics
import pandas as pd
import matplotlib.pyplot as plt


def error_analysis(file_name, date_name="timestamp", prediction_name="prediction_value", ground_truth_name="ground_truth", sensor_name="location"):
    if date_name:
        df=pd.read_csv(file_name, parse_dates=[date_name], infer_datetime_format=True)
    else:
        df = pd.read_csv(file_name)
    metrics= get_all_metrics(df, ground_truth_name, prediction_name)
    for metric in metrics:
        print("%s: %s"%(metric, metrics[metric]))

    if date_name:
        df.set_index(date_name, inplace=True)
        sensors=df.groupby([sensor_name])
        i=0
        for sensor_id in sensors.groups.keys():
            node = sensors.get_group(sensor_id)
            ax=plt.subplot(len(sensors.groups.keys()), 1, 1+i)
            node[[ground_truth_name, prediction_name]].plot( title="node:" + str(sensor_id), ax=ax)
            i += 1
        plt.show()

if __name__ == '__main__':
    #error_analysis("utah_171101_180101_validation_ppa_ppa_pm25_6_0.01/prediction.csv")
    error_analysis("utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction.csv")
    #error_analysis("original_prediction.csv", date_name=None)
    #error_analysis("utah_171101_180101_dl_ppa_epa_pm25_8_0.01/prediction.csv", date_name="date_observed", prediction_name="predictions", ground_truth_name="value", sensor_name="station_id")

