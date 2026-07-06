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

def find_missing_first_name(employees):
    count=0
    for line in employees:
        first_name=line["first_name"]
        cleaned_first_name=len(first_name.strip())
        if cleaned_first_name==0:
            count+=1
    return count


def main():
    employees = load_csv()
    total_rows = count_rows(employees)
    total_columns= count_columns(employees)
    first_name=find_missing_first_name(employees)
    # print(employees)
    print(f"Total rows present in the current DataSet is : {total_rows}")
    print(f"Total columns present in the current DataSet is : {total_columns}")
    print(f"Count of Missing First Name  : {first_name}")

main()