from data_management.data_loader import DataLoader
from data_analysis.data_analysis import DataAnalysis


dataset_path = "C:/Users/Camilo Guillen/Documents/Universidad de los Andes/2021-2/Asistencia Graduada" \
                        " 2021-2/Datos IDEAM/datos"
variable = 'vel_viento'
frequency = 'horaria'
department = 'la_guajira'
city = 'riohacha'
year = 2000
all_months = True
month = 8
method = 'MCD'

data_loader = DataLoader(path=dataset_path, variable=variable, frequency=frequency)
data_analysis = DataAnalysis(data_loader=data_loader, department=department, city=city, year=year)
data_analysis.run(all_months=all_months, month=month, method=method, title=" ".join([method, variable, frequency]),
                  y_label="Variable value", x_label="Day of year")
