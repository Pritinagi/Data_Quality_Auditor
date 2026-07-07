import csv
def load_csv():
    
    with open("employee_data.csv","r") as csv_file:
        csv_reader=csv.DictReader(csv_file)
        employees=[]

        for line in csv_reader:
            employees.append(line)

        return employees