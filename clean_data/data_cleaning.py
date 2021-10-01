class DataCleaning:
    def __init__(self, dataset, department, city, year, all_departments=False, all_cities=False):
        self.data = dataset.get_data(department=department, cities=[city], all_departments=all_departments,
                                     all_cities=all_cities, years=[year])

    def remove_nan_values(self):
        data = self.data
        self.data = data.dropna(subset=['Value'], inplace=False)

        return self.data

    def remove_negatives(self):
        data = self.data
        self.data = data[(data[['Value']] >= 0).all(1)]

        return self.data

    def remove_duplicate_values(self):
        data = self.data
        self.data = data.drop_duplicates(subset=['Department', 'City', 'Latitude', 'Longitude', 'Altitude', 'Day',
                                                 'Month', 'Year', 'Hour'], keep='first', inplace=False)

        return self.data

    def remove_constants_values(self):
        data = self.data
        available_dates = data['Date'].unique()
        idx = list()
        for date in available_dates:
            all_values_per_date = data[data['Date'] == date]['Value']
            if all_values_per_date.eq(all_values_per_date.iloc[0]).all():
                [idx.append(i) for i in list(all_values_per_date.index)]

        self.data = data.drop(idx)

        return self.data

    def run(self):
        self.remove_nan_values()
        self.remove_negatives()
        # self.remove_duplicate_values()
        self.remove_constants_values()
        self.data.reset_index(inplace=True)

        return self.data
