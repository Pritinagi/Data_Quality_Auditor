import csv
from datetime import datetime

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
    if not employees:
        return 0
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
    count_missing_row=0
    for line in employees:
        column_value=line[column_name]
        cleaned_column_value=len(column_value.strip())
        if cleaned_column_value==0:
            count_missing_row+=1
    return count_missing_row

def find_invalid_emails(employees):
    count_invalid_email =0
    for line in employees:
        email=line["email"]
        value_error_1=email.count('@')
        cleaned_email=len(email.strip())
        if cleaned_email==0:
            continue      
        elif '@' not in email:
             count_invalid_email+=1
        elif value_error_1>1 :
            count_invalid_email+=1
        else:
            parts = email.split("@")
            part_1=len(parts[0])
            part_2=len(parts[1])
            part_2_value=parts[1].count(".")
            if part_1==0 or part_2==0:
                count_invalid_email+=1    
            elif part_2_value<1:
                count_invalid_email+=1       
    return count_invalid_email

def find_invalid_age(employees):
    count_invalid_age=0
    for line in employees:
        age=line["age"]
        # cleaned_age=len(age.strip())
        # if cleaned_age==0:
        if not age:
            continue
        try:
            int_age=int(age)
        except ValueError:
            count_invalid_age+=1
        else :
            if int_age < 18 or int_age > 65:
                count_invalid_age += 1

        # it is an alternative
        # if age.isnumeric():
        #     int_age=int(line["age"])
        #     if int_age < 18 or int_age > 65:
        #         count_invalid_age += 1
    return count_invalid_age

def find_invalid_salary(employees):
    count_invalid_salary=0
    for line in employees:
        salary_str=line["salary"]
        cleaned_salary=len(salary_str.strip())
        if cleaned_salary==0:
            continue
        try:
            salary_int=int(salary_str)
        except ValueError:
            count_invalid_salary+=1
        else:
            if salary_int < 1 or salary_int > 500000:
                count_invalid_salary+=1

    return count_invalid_salary


# helpful with date and time
def find_invalid_joining_date(employees):
    count_invalid_dates=0
    
    for line in employees:
        
        joining_dates=line["joining_date"]
        cleaned_date=len(joining_dates.strip())
        if cleaned_date==0:
            continue
        try:
            datetime.strptime(joining_dates,"%m/%d/%Y")
        except ValueError:
            count_invalid_dates+=1
    return count_invalid_dates

# def find_duplicate_values(employees, column_name):
#     seen=set()
#     duplicate=set()
#     count_duplicate_entry=0
#     count_seen={}
#     for line in employees:
        
#         column_value=line[column_name]
#         cleaned_column_value=column_value.strip()
#         if not cleaned_column_value:
#             continue
#         elif cleaned_column_value in seen:
#             duplicate.add(cleaned_column_value)
#             count_duplicate_entry+=1
#             count_seen[cleaned_column_value]=count_seen.get(cleaned_column_value,0)+1
#         else:
#             seen.add(cleaned_column_value)
#     return count_duplicate_entry,count_seen




# a new fnction for find_duplicate_values 
def find_duplicate_values(employees,  column_name):
    occurrence={}
    duplicate={}
    for line in employees:
        column_value=line[ column_name]
        cleaned_column_data= column_value.strip()
        if not cleaned_column_data:
            continue
        else:
            occurrence[cleaned_column_data]=occurrence.get(cleaned_column_data,0)+1
    for value, count in occurrence.items():
                if count>1:
                    duplicate[value]=count
    return duplicate




def main():

    employees = load_csv()
    total_rows = count_rows(employees)
    total_columns= count_columns(employees)
    total_invalid_emails=find_invalid_emails(employees)
    total_invalid_age= find_invalid_age(employees)
    total_invalid_salary=find_invalid_salary(employees)
    total_invalid_joining_date=find_invalid_joining_date(employees)


    # count_missing_first_name=find_missing_first_name(employees)
    # column_name=input("Enter column name...\n The options you have is : id | first_name | last_name | email | gender | country | joining_date | salary | department | age ")
   

    # print(employees)
    print("="*30 )
    print("Data Quality Check")
    print("="*30 )

    print("Dataset Summary")
    print("-"*30 )
    
    print(f"Total rows present in the current DataSet is : {total_rows:<25}")
    print(f"Total columns present in the current DataSet is : {total_columns:<20}")
    missing_columns= [
        "first_name","last_name","email","gender","joining_date","department"
        # add the name of columne you want to check out 
    ]
    print("-"*30 )
    for missing_column in missing_columns:
        column_missing_values =find_missing_values(employees,missing_column )
        print(f"Missing values in {missing_column:<20} is {column_missing_values:<20}")

    # print(f"Count of Missing First Name  : {count_missing_first_name}")
    # print(f"Count of missing values in {column_name} is {column_missing_values}")
    print(f"Invalid emails {total_invalid_emails} ")
    print(f"Invalid age {total_invalid_age} ")
    print(f"Invalid salary {total_invalid_salary} ")
    print(f"Invalid Joining Date {total_invalid_joining_date} ")
    
    column_name= [
            "first_name","last_name","email","joining_date","department"
            # add the name of columne you want to check out 
        ]
    

    for duplicate_column in  column_name:
        duplicate=find_duplicate_values(employees,duplicate_column)
        duplicate_items_found=len(duplicate)
        # print("="*30)
        print(f"column : {duplicate_column}")
        print(f"Duplicate items : {duplicate_items_found}")
        
        print("Duplicate items and their occurrences ")
        print("="*30 )

        # for total_dupliacte in occurrence.items():
        if duplicate:
            for value,count in duplicate.items():
                print(f"{value:<20} : {count}")
        else:
            print("No duplicates found")
        print("-"*30 ,"\n")
        
            
            # total_invalid_column_details, count_seen_for_every_duplicate=find_duplicate_values(employees,column_name)
            # print(f"Count of duplicate data in : {column_name}\n duplicate occurence : {total_invalid_column_details}\n and the duplicate values are : {count_seen_for_every_duplicate}")



main()