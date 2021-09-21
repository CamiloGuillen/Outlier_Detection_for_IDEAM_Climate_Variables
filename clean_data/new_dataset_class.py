import os

from clean_data.data_cleaning import DataCleaning
from clean_data.outlier_detection import OutlierDetection
from tqdm import tqdm


class NewDataset:
    def __init__(self, department, city, data_loader, variable, frequency):
        self.department = department
        self.city = city
        self.data_loader = data_loader
        self.variable = variable
        self.frequency = frequency

    def run_clean_data_process(self, year):
        data_clean_obj = DataCleaning(dataset=self.data_loader, department=self.department, city=self.city, year=year)
        new_data = data_clean_obj.run()

        return new_data

    def run_remove_outlier_process(self, year, features, method):
        clean_data = self.run_clean_data_process(year=year)
        outlier_detection_obj = OutlierDetection(data=clean_data, features=features, method=method)
        new_data = outlier_detection_obj.remove_outliers()

        return new_data

    def save_data(self, path, year, data):
        if not os.path.exists(path):
            os.mkdir(path)

        departments = data['Department'].unique()
        for department in departments:
            path_lvl_1 = os.path.join(path, department.lower())

            if department.lower() == "archipielago de san andres, providencia y santa catalina":
                path_lvl_1 = os.path.join(path, "archipielago de san andres")

            if not os.path.exists(path_lvl_1):
                os.mkdir(path_lvl_1)

            department_data = data[data['Department'] == department]
            cities = department_data['City'].unique()
            for city in cities:
                path_lvl_2 = os.path.join(path_lvl_1, city.lower())
                if not os.path.exists(path_lvl_2):
                    os.mkdir(path_lvl_2)
                path_lvl_3 = os.path.join(path_lvl_2, self.variable)
                if not os.path.exists(path_lvl_3):
                    os.mkdir(path_lvl_3)
                path_lvl_4 = os.path.join(path_lvl_3, self.frequency)
                if not os.path.exists(path_lvl_4):
                    os.mkdir(path_lvl_4)

                city_info = department_data[department_data['City'] == city]
                file_name = os.path.join(path_lvl_4, f'{year}.csv')
                city_info.to_csv(file_name, index=False, index_label=False, sep=';')

    def run(self, years, features, method, path):
        for year in tqdm(years):
            new_data = self.run_remove_outlier_process(year=year, features=features, method=method)
            self.save_data(path=path, year=year, data=new_data)

        return True
