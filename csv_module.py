import csv
with open('csv/csv1.csv','r') as file:
    data = list(csv.reader(file))
#print(data)
search = input("Ente text to search: ")
for row in data:
    #print(row)
    if row[1]==search:
        print(row[0])
