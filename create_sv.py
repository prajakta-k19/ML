import csv

data = [
    ['A', 'B', 'C','D','E'],
    ['Adya', 21, 'Bbsr', '1234567890','23053092'],
    ['Varun', 32, ' Pune', '0987654321','23052611'],
    ['Shambhavi', 22 , 'Bihar', '831012','23052811']
]

with open('main.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("CSV file 'main.csv' created successfully.")