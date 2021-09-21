import os
import pandas as pd


class DataLoader:
    def __init__(self, path, variable, frequency):
        self.path = path
        self.variable = variable
        self.frequency = frequency

    def get_data(self, all_departments=False, department=None, all_cities=False, cities=None, all_years=False,
                 years=None):
        list_df = list()

        if all_departments:
            departments = os.listdir(self.path)
        else:
            departments = [department]

        for department in departments:
            lvl_1_path = os.path.join(self.path, department)
            if all_cities:
                cities = os.listdir(lvl_1_path)

            for city in cities:
                lvl_2_path = os.path.join(lvl_1_path, city, self.variable, self.frequency)
                if all_years:
                    years = os.listdir(lvl_2_path)
                    years = [int(str(year).split('.')[0]) for year in years]

                for year in years:
                    full_path = os.path.join(lvl_2_path, f"{year}.csv")
                    if os.path.exists(full_path):
                        df_data = pd.read_csv(full_path)
                        list_df.append(df_data[['Departamento', 'Municipio', 'Latitud', 'Longitud', 'Altitud', 'Fecha',
                                                'Valor']].copy())

        if list_df:
            data = pd.concat(list_df, ignore_index=True)

            data['Hour'] = data['Fecha'].apply(lambda x: x.split(' ')[1])
            data['Date'] = data['Fecha'].apply(lambda x: x.split(' ')[0])

            data['Day'] = data['Date'].apply(lambda x: int(x.split('-')[2]))
            data['Month'] = data['Date'].apply(lambda x: int(x.split('-')[1]))
            data['Year'] = data['Date'].apply(lambda x: int(x.split('-')[0]))
            data['Hour'] = data['Hour'].apply(lambda x: int(x.split(':')[0]))

            data.rename(columns={'Departamento': 'Department', 'Municipio': 'City', 'Latitud': 'Latitude',
                                 'Longitud': 'Longitude', 'Altitud': 'Altitude', 'Valor': 'Value'}, inplace=True)

            data = data[['Department', 'City', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Day', 'Month', 'Year',
                         'Hour', 'Value']]
        else:
            data = pd.DataFrame(columns=['Department', 'City', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Day',
                                         'Month', 'Year', 'Hour', 'Value'])

        return data


class DataLoader2:
    def __init__(self, path, variable, frequency):
        self.path = path
        self.variable = variable
        self.frequency = frequency

    def get_data(self, all_departments=False, department=None, all_cities=False, cities=None, all_years=False,
                 years=None):
        list_df = list()

        if all_departments:
            departments = os.listdir(self.path)
        else:
            departments = [department]

        for department in departments:
            lvl_1_path = os.path.join(self.path, department)
            if all_cities or all_departments:
                cities = os.listdir(lvl_1_path)

            for city in cities:
                lvl_2_path = os.path.join(lvl_1_path, city, self.variable, self.frequency)
                if all_years:
                    years = os.listdir(lvl_2_path)
                    years = [int(str(year).split('.')[0]) for year in years]

                for year in years:
                    full_path = os.path.join(lvl_2_path, f"{year}.csv")
                    if os.path.exists(full_path):
                        df_data = pd.read_csv(full_path)
                        list_df.append(df_data)

        if list_df:
            data = pd.concat(list_df, ignore_index=True)
        else:
            data = pd.DataFrame(columns=['Department', 'City', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Day',
                                         'Month', 'Year', 'Hour', 'Value'])

        return data
