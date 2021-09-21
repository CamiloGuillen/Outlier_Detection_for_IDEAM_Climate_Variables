import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from clean_data.outlier_detection import OutlierDetection


class DataAnalysis:
    def __init__(self, data_loader, department, city, year):
        self.year_data = data_loader.get_data(department=department, cities=[city], years=[year])
        self.missing_data = list()
        self.year_24_hours_data = list()
        self.all_outliers = list()

    def find_missing_data(self, all_months=False, month=1, variable='Value'):
        if all_months:
            all_months = self.year_data['Month'].unique()
            range_months = range(1, 12)
        else:
            all_months = [month]
            range_months = range(month, month + 1)

        year_24_hours_data, missing_data = list(), list()
        for month in range_months:
            if month in all_months:
                month_data = self.year_data[self.year_data['Month'] == month]

                all_days = month_data['Day'].unique()
                for day in range(1, 31):
                    hours = list()
                    hour_data = np.zeros(24)

                    if day in all_days:
                        day_data = month_data[month_data['Day'] == day].reset_index()
                        values_data = day_data[variable].values
                        hours = day_data['Hour'].values
                        for i, j in enumerate(hours):
                            hour_data[j] = values_data[i]

                    year_24_hours_data.append(hour_data)
                    missing_data.append([i for i in range(24) if i not in hours])
            else:
                for day in range(30):
                    year_24_hours_data.append(np.zeros(24))
                    missing_data.append(list(range(24)))

        year_24_hours_data = np.concatenate(year_24_hours_data)
        all_missing_data = list()
        for i, data in enumerate(missing_data):
            for day in data:
                all_missing_data.append(day + 24 * i)

        return year_24_hours_data, all_missing_data

    @staticmethod
    def find_outliers(data, method):
        data = pd.DataFrame(data=data, columns=['Value'])
        outlier_detector = OutlierDetection(data=data, features='Value', method=method)
        idx = outlier_detector.detect_outliers()

        return idx

    def run(self, all_months=False, month=1, variable='Value', method='MCD', title="", x_label="", y_label=""):
        new_data, missing_data_idx = self.find_missing_data(all_months=all_months, month=month, variable=variable)
        outliers_idx = self.find_outliers(data=new_data, method=method)

        plt.figure()
        plt.plot(new_data, c='cyan', lw=0.5)
        for idx in missing_data_idx:
            plt.axvline(idx, c='grey', ls='--', lw=0.2)
        for idx in outliers_idx:
            plt.scatter(x=idx, y=new_data[idx], c='r', s=4)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        return missing_data_idx, outliers_idx
