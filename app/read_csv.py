#Modulo para leer el archivo CSV

import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      country_dict = {headers:values for headers,values in zip(header,row)}
      data.append(country_dict) 
  return data  

def read_row_csv(data):
  world_percent = {}
  for row in data:
    world_percent.update({row['Country/Territory']:float(row['World Population Percentage'])})
  labels =  list(world_percent.keys())
  values = list(world_percent.values())
  return labels, values

  
#EJECUTANDO EL MODULO COMO UN SCRIPT DIRECTAMENTE.
if __name__ == '__main__':
  print('EJECUTANDO EL SCRIPT DIRECTAMENTE')

  
