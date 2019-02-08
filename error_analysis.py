from evaluation import get_all_metrics
import pandas as pd
import matplotlib.pyplot as plt
import os


def error_analysis(file_path, date_name="timestamp", prediction_name="prediction_value",
                   ground_truth_name="ground_truth", sensor_name="location"):
    if date_name:
        df = pd.read_csv(file_path, parse_dates=[date_name], infer_datetime_format=True)
    else:
        df = pd.read_csv(file_path)

    metrics = get_all_metrics(df, ground_truth_name, prediction_name)
    for metric in metrics:
        print("%s: %s" % (metric, metrics[metric]))

    if date_name:
        df.set_index(date_name, inplace=True)
        min_val = df[[ground_truth_name, prediction_name]].min(skipna=True).min()
        max_val = df[[ground_truth_name, prediction_name]].max(skipna=True).max()

        sensors = df.groupby([sensor_name])

        f = plt.figure(figsize=(20, 10))

        i = 0
        for sensor_id in sensors.groups.keys():
            node = sensors.get_group(sensor_id)
            ax = f.add_subplot(len(sensors.groups.keys()), 1, 1 + i)
            node[[ground_truth_name, prediction_name]].plot(title="station:" + str(sensor_id), ax=ax,
                                                            ylim=(min_val, max_val))
            i += 1

        # for sensor_id in sensors.groups.keys():
        #     node = sensors.get_group(sensor_id)
        #     ax = plt.subplot(len(sensors.groups.keys()), 1, 1 + i)
        #     node[[ground_truth_name, prediction_name]].plot(title="station:" + str(sensor_id), ax=ax,
        #                                                     ylim=(min_val, max_val))
        #     i += 1

        file_name = os.path.dirname(file_path)
        path_to_save = os.path.dirname(file_name)
        picture_path = os.path.join(path_to_save, file_name + ".png")
        text_path = os.path.join(path_to_save, file_name + ".txt")

        f.savefig(picture_path, bbox_inches="tight")
        with open(text_path, "w") as f:
            f.write(str(metrics))


if __name__ == '__main__':
    # error_analysis("utah_171101_180101_validation_ppa_ppa_pm25_6_0.01/prediction.csv")
    # error_analysis("utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction.csv")

    # error_analysis("original_prediction.csv", date_name=None)

    # error_analysis("utah_171101_180101_dl_ppa_epa_pm25_8_0.01/prediction.csv", date_name="date_observed", prediction_name="predictions", ground_truth_name="value", sensor_name="station_id")

    # error_analysis("utah_180201_180401_validation_ppa_epa_pm25_6_0.01/prediction.csv")
    # error_analysis("utah_180201_180401_validation_ppa_ppa_pm25_6_0.01/prediction.csv")

    # error_analysis("utah_180501_180601_validation_ppa_epa_pm25_6_0.01/prediction.csv")
    # error_analysis("utah_180501_180601_validation_ppa_ppa_pm25_6_0.01/prediction.csv")
    #
    # error_analysis("utah_171101_180101_validation_ppa_ppa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")
    #
    # error_analysis("utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")
    #
    #
    #
    # error_analysis("utah_180201_180401_validation_ppa_ppa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")
    #
    # error_analysis("utah_180201_180401_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")
    #
    # error_analysis("utah_180501_180601_validation_ppa_ppa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")
    #
    # error_analysis("utah_180501_180601_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")

    # error_analysis("utah_1711_1806_validation_ppa_epa_pm25_w_6hr/prediction_new.csv",
    #                ground_truth_name="smoothed_ground_truth",
    #                sensor_name="location",
    #                prediction_name="prediction_value",
    #                date_name="timestamp")

    dirs = ['utah_1711_1806_validation_ppa_epa_pm25_w_6hr',
            'utah_1711_1806_validation_ppa_epa_pm25_6hr',
            'utah_1711_1806_validation_ppa_ppa_pm25_6hr',
            'utah_1711_1806_validation_ppa_ppa_pm25_w_6hr',
            'utah_1711_180601_validation_ppa_epa_pm25_w'
            ]

    # working_dir = os.getcwd()
    # for d in dirs:
    #     p = os.path.join(working_dir, d)
    #     months = os.listdir(p)
    #     months= list(filter(lambda x: not( x.endswith(".txt") or x.endswith(".png") or x.endswith(".csv")), months ) )
    #     months.sort()
    #     for month in months:
    #         tmp_path = os.path.join(p, month, "prediction.csv")
    #         print(d)
    #         error_analysis(tmp_path, date_name="date_observed",
    #                        prediction_name="predictions", ground_truth_name="value",
    #                        sensor_name="station_id")

    working_dir = os.getcwd()
    for d in dirs:
        p = os.path.join(working_dir, d)
        months = os.listdir(p)
        months = list(filter(lambda x: not (x.endswith(".txt") or x.endswith(".png") or x.endswith(".csv")), months))
        months.sort()
        file_names = []
        for month in months:
            tmp_path = os.path.join(p, month, "prediction.csv")
            file_names.append(tmp_path)
        df = pd.concat([pd.read_csv(f) for f in file_names])
        all_predictions_path=os.path.join(p, "all_predictions.csv")
        df.to_csv(all_predictions_path)

        error_analysis(all_predictions_path, date_name="date_observed",
                       prediction_name="predictions", ground_truth_name="value",
                       sensor_name="station_id")
