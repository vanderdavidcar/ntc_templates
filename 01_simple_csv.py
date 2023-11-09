import csv

"""
This is the simple way to create a csv file
"""
with open('names.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]
    
    writer.writerow(field)
    writer.writerow(["Marcelo Kitana", "40", "Brazil"])
    writer.writerow(["Aline Kuoko", "23", "Japan"])
    writer.writerow(["Tamiris Walter", "50", "United Kingdom"])