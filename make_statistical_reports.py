from data_management.data_loader import DataLoader, DataLoader2
from data_analysis.statistical_report import StatisticalReport

variable = 'rad_solar'
frequency = 'diaria'
years = range(1998, 2020)

original_dataset_path = "C:/Users/Camilo Guillen/Documents/Universidad de los Andes/2021-2/Asistencia Graduada" \
                        " 2021-2/Datos IDEAM/datos"
iForest_dataset_path = "new_dataset/iForest"
mcd_dataset_path = "new_dataset/MCD"
lof_dataset_path = "new_dataset/LOF"

original_data_loader = DataLoader(path=original_dataset_path, variable=variable, frequency=frequency)
iForest_data_loader = DataLoader2(path=iForest_dataset_path, variable=variable, frequency=frequency)
mcd_data_loader = DataLoader2(path=mcd_dataset_path, variable=variable, frequency=frequency)
lof_data_loader = DataLoader2(path=lof_dataset_path, variable=variable, frequency=frequency)

original_report_obj = StatisticalReport(data_loader=original_data_loader, years=years)
original_report_obj.make_and_save_report(path=f"statistical_report/original/{variable}/{frequency}")

iForest_report_obj = StatisticalReport(data_loader=iForest_data_loader, years=years)
iForest_report_obj.make_and_save_report(path=f"statistical_report/iForest/{variable}/{frequency}")

mcd_report_obj = StatisticalReport(data_loader=mcd_data_loader, years=years)
mcd_report_obj.make_and_save_report(path=f"statistical_report/MCD/{variable}/{frequency}")

lof_report_obj = StatisticalReport(data_loader=lof_data_loader, years=years)
lof_report_obj.make_and_save_report(path=f"statistical_report/LOF/{variable}/{frequency}")
