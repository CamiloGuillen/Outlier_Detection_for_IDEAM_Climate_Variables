import os

from data_management.data_loader import DataLoader
from clean_data.new_dataset_class import NewDataset

dataset_path = "/home/camilo/Documents/Universidad de los Andes/2021-2/Asistencia Graduada 2021-2/Datos IDEAM/datos"
variable = 'temp'
frequency = 'horaria'
data_loader = DataLoader(path=dataset_path, variable=variable, frequency=frequency)

methods = ['LOF']
features = ['Value']
years = range(1998, 2020)

all_departments = sorted(os.listdir(dataset_path))
for method in methods:
    for department in all_departments:
        cities = sorted(os.listdir(os.path.join(dataset_path, department)))
        for city in cities:
            print("-"*50)
            print(f"Method: {method} | Department: {department} | City: {city}")
            new_dataset_obj = NewDataset(data_loader=data_loader, variable=variable, frequency=frequency,
                                         department=department, city=city)
            new_dataset_obj.run(years=years, features=features, method=method, path=f"dataset_clean/{method}")
            print(" ")
