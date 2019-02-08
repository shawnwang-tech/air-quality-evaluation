import pandas as pd
import os
from data_preprocess import timeseries_utils

def moving_average(in_name, out_name, ground_truth, prediction_name, date_name, station_name):
    timeseries_utils.TIME_COL=date_name
    timeseries_utils.KEY_COL=station_name

    df=pd.read_csv(in_name, parse_dates=[date_name], infer_datetime_format=True)
    predictions=df[prediction_name].copy()
    previous=df[ground_truth].copy()

    ts=timeseries_utils.time_series_construction(df, value_col=ground_truth)


    ts=timeseries_utils.time_series_smoothing(ts, window_size=24)
    ts.reset_index(inplace=True)
    ts.rename(columns={"index": "timestamp"}, inplace=True)

    tmp = []
    for column in ts:
        if column == "timestamp":
            continue
        station = ts[[column, "timestamp"]]
        station["location"] = column
        station = station.rename(columns={column: "smoothed_ground_truth"})
        tmp.append(station)

    df=pd.concat(tmp, ignore_index=True)

    df.sort_values(by=['timestamp', "location"], inplace=True)
    df.reset_index(inplace=True, drop=True)

    df["prediction_value"]=predictions
    df["original_ground_truth"]=previous

    df.to_csv(out_name, index=False)

# moving_average("../utah_180201_180401_validation_ppa_epa_pm25_6_0.01/prediction.csv",
#                "../utah_180201_180401_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
#                ground_truth="ground_truth",
#                prediction_name="prediction_value",
#                date_name="timestamp",
#                station_name="location")

# moving_average("../utah_180201_180401_validation_ppa_ppa_pm25_6_0.01/prediction.csv",
#                "../utah_180201_180401_validation_ppa_ppa_pm25_6_0.01/prediction_new.csv",
#                ground_truth="ground_truth",
#                prediction_name="prediction_value",
#                date_name="timestamp",
#                station_name="location")

# moving_average("../utah_180501_180601_validation_ppa_ppa_pm25_6_0.01/prediction.csv",
#                "../utah_180501_180601_validation_ppa_ppa_pm25_6_0.01/prediction_new.csv",
#                ground_truth="ground_truth",
#                prediction_name="prediction_value",
#                date_name="timestamp",
#                station_name="location")

# moving_average("../utah_180501_180601_validation_ppa_epa_pm25_6_0.01/prediction.csv",
#                "../utah_180501_180601_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
#                ground_truth="ground_truth",
#                prediction_name="prediction_value",
#                date_name="timestamp",
#                station_name="location")

# moving_average("../utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction.csv",
#                "../utah_171101_180101_validation_ppa_epa_pm25_6_0.01/prediction_new.csv",
#                ground_truth="ground_truth",
#                prediction_name="prediction_value",
#                date_name="timestamp",
#                station_name="location")

moving_average("../utah_171101_180101_dl_ppa_epa_pm25_8_0.01/prediction_tmp.csv",
               "../utah_171101_180101_dl_ppa_epa_pm25_8_0.01/prediction_new.csv",
               ground_truth="ground_truth",
               prediction_name="prediction_value",
               date_name="timestamp",
               station_name="location")
