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

# def find_missing_first_name(employees):
#     count=0
#     for line in employees:
#         first_name=line["first_name"]
#         cleaned_first_name=len(first_name.strip())
#         if cleaned_first_name==0:
#             count+=1
#     return count

def find_missing_values(employees, column_name):
    count=0
    for line in employees:
        column_value=line[column_name]
        cleaned_column_value=len(column_value.strip())
        if cleaned_column_value==0:
            count+=1
    return count

def find_invalid_emails(employees):
    count =0
    for line in employees:
        email=line["email"]
        value_error_1=email.count('@')
        cleaned_email=len(email.strip())
        if cleaned_email==0:
            continue      
        elif '@' not in email:
             count+=1
        elif value_error_1>1 :
            count+=1
        else:
            parts = email.split("@")
            part_1=len(parts[0])
            part_2=len(parts[1])
            part_2_value=parts[1].count(".")
            if part_1==0 or part_2==0:
                count+=1    
            elif part_2_value<1:
                count+=1       
    return count



def main():

    employees = load_csv()
    total_rows = count_rows(employees)
    total_columns= count_columns(employees)
    total_invalid_emails=find_invalid_emails(employees)
    # count_missing_first_name=find_missing_first_name(employees)
    # column_name=input("Enter column name...\n The options you have is : id | first_name | last_name | email | gender | country | joining_date | salary | department | age ")
    

    # print(employees)
    print(f"Total rows present in the current DataSet is : {total_rows}")
    print(f"Total columns present in the current DataSet is : {total_columns}")
    column_names= [
        "first_name","last_name","email","gender","joining_date","department"
        # add the name of columne you want to check out 
    ]
    for column_name in column_names:
        column_missing_values =find_missing_values(employees,column_name )
        print(f"Count of missing values in {column_name} is {column_missing_values}")
    # print(f"Count of Missing First Name  : {count_missing_first_name}")
    # print(f"Count of missing values in {column_name} is {column_missing_values}")
    print(f"Count of invalid emails {total_invalid_emails} ")

main()