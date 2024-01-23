import utils, read_csv, charts 

def run_main():
  while True:
    try: 
      data = read_csv.read_csv('./data.csv')
      name = input('Type country => ').title()
      country_dict = utils.population_by_country(data,name)
      if len(country_dict) != 1:
        raise Exception('Pais no encontrado.') 
      else:
        break
    except Exception:
      print('Lo sentimos, no se encontro el pais.')
    
  keys, values = utils.get_population(country_dict[0])
  charts.generate_bar_chart(keys,values,name) # Comentar esta linea si deseas correr el grafico tipo pie.
  
  data = filter(lambda item: item['Continent'] == 'South America', data)
  labels, percents = read_csv.read_row_csv(data)
  charts.generate_pie_chart(labels,percents) #Quitar comentario para usar la funcion tipo pie.


if __name__ == '__main__':
  run_main()