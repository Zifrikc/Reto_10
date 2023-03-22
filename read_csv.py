import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data



    column_index = next(reader).index('World Population Percentage')
    column_values = []
    for row in reader:

      column_values.append(row[column_index]) 
    return column_values

if __name__ == '__main__':
  data = read_csv('./app2/data2.csv')
  print(data[0])