#Modulo para obtener la poblacion de un pais.

def get_population(country_dict):
  years_filtered = {}
  for item in country_dict:
    if item.endswith('Population'):
      years_filtered.update({item:country_dict[item]})
  years_population = {key[:-11]:value for key,value in years_filtered.items()}
  keys = list(years_population.keys())
  for item in years_population:
    years_population[item] = int(years_population[item])
  values = list(years_population.values())
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result
  
if __name__ == '__main__' : 
  print('EJECUTANDO EL SCRIPT DIRECTAMENTE')

  
