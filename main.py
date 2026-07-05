import csv
def load_csv():
    with open("employee_data.csv","r") as csv_file:
        csv_reader=csv.DictReader(csv_file)
        employees=[]
        for line in csv_reader:
            employees.append(line)
        return employees
            # print(line)
def count_rows(employees):
    total_rows=len(employees)
    return total_rows

def count_columns(employees):
    first_employee=employees[0]
    total_columns=len(first_employee)
    return total_columns

def main():
    employees = load_csv()
    total_rows = count_rows(employees)
    total_columns= count_columns(employees)
    # print(employees)
    print(f"Total rows present in the current DataSet is : {total_rows}")
    print(f"Total columns present in the current DataSet is : {total_columns}")



main()