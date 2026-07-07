from data_loader import load_csv 
from validators import find_missing_values, find_invalid_age, find_invalid_salary,find_invalid_joining_date, find_invalid_emails, find_duplicate_values
from report_generator import generate_report

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
    
    # gnerating report
    generate_report(
        employees,
    total_rows,
    total_columns,
    total_invalid_emails,
    total_invalid_age,
    total_invalid_salary,
    total_invalid_joining_date
)


main()

