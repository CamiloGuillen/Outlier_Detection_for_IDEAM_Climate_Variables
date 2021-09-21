import os
import pandas as pd

from tqdm import tqdm


class StatisticalReport:
    def __init__(self, data_loader, years):
        self.data_loader = data_loader
        self.years = years

    def make_report(self):
        print("Making report ...")

        max_per_year = dict()
        min_per_year = dict()
        mean_per_year = dict()
        std_per_year = dict()
        for year in tqdm(self.years):
            data = self.data_loader.get_data(all_departments=True, all_cities=True, years=[year])
            departments = data["Department"].unique()

            max_per_department = dict()
            min_per_department = dict()
            mean_per_department = dict()
            std_per_department = dict()
            for department in departments:
                values = data[data['Department'] == department]["Value"].values
                max_per_department[department] = values.max()
                min_per_department[department] = values.min()
                mean_per_department[department] = values.mean()
                std_per_department[department] = values.std()

            max_per_year[year] = max_per_department
            min_per_year[year] = min_per_department
            mean_per_year[year] = mean_per_department
            std_per_year[year] = std_per_department

        return max_per_year, min_per_year, mean_per_year, std_per_year

    def make_and_save_report(self, path):
        max_per_year, min_per_year, mean_per_year, std_per_year = self.make_report()

        print("Saving report ...")
        years = list(max_per_year.keys())
        reports = dict()
        for year in tqdm(years):
            reports[year] = pd.DataFrame()
            reports[year]['Department'] = list(max_per_year[year].keys())
            reports[year]['Max'] = list(max_per_year[year].values())
            reports[year]['Min'] = list(min_per_year[year].values())
            reports[year]['Mean'] = list(mean_per_year[year].values())
            reports[year]['Std'] = list(std_per_year[year].values())

            path_lvl_1 = path.split('/')[0]
            if not os.path.exists(path_lvl_1):
                os.mkdir(path_lvl_1)
            path_lvl_2 = os.path.join(path_lvl_1, path.split('/')[1])
            if not os.path.exists(path_lvl_2):
                os.mkdir(path_lvl_2)
            path_lvl_3 = os.path.join(path_lvl_2, path.split('/')[2])
            if not os.path.exists(path_lvl_3):
                os.mkdir(path_lvl_3)
            path_lvl_4 = os.path.join(path_lvl_3, path.split('/')[3])
            if not os.path.exists(path_lvl_4):
                os.mkdir(path_lvl_4)
            reports[year].to_csv(os.path.join(path, f"{str(year)}.csv"), index=False)

        return reports
