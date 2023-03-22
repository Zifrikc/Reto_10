import utilies
import read_csv
import cha

def run():
  data = read_csv.read_csv('./app2/data2.csv')
  # filtrar por datos solo de sudamerica
  data = list(filter(lambda item : item['Continent']== 'South America',data))

  countries = list(map(lambda x : x['Country'], data))
  percentages = list(map(lambda x : x['World Population Percentage'],data))
  cha.generate_bar_chart(countries, percentages)
  '''
  country =  input('Type Country = >')
  
  result = utilies.population_by_country(data, country)
   
  if len(result) > 0:
    country = result[0]
    labels, values = utilies.get_population(country)
    cha.generate_bar_chart(labels, values)
 ''' 

if __name__ == '__main__':
  run()