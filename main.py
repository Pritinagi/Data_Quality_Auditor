from data_loader import load_csv 
from validators import find_missing_values, find_invalid_age, find_invalid_salary,find_invalid_joining_date, find_invalid_emails, find_duplicate_values
from report_generator import generate_report
from logger_config import logger



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
    #===========Function call==============#
    logger.info("Data Quality Auditor started.")
    employees = load_csv()
    total_rows = count_rows(employees)
    total_columns= count_columns(employees)

    # =====Email Validation=======
    logger.info("Checking Email Validation")

    total_invalid_emails=find_invalid_emails(employees)
    if total_invalid_emails==0:
            logger.info("No Invalid EMAIL Found")
    else:
        logger.warning("Found %d Invalid EMAIL(S)",total_invalid_emails)


    # =========Invalid AGE=============  
    logger.info("Checking AGE Validation")

    total_invalid_age= find_invalid_age(employees)
    if total_invalid_age==0:
            logger.info("No Invalid AGE Found")
    else:
        logger.warning("Found %d Invalid AGE(S)",total_invalid_age)


    # ==========Invalid SALARY===============
    logger.info("Checking SALARY Validation")

    total_invalid_salary=find_invalid_salary(employees)
    if total_invalid_salary==0:
            logger.info("No Invalid SALARY Found")
    else:
        logger.warning("Found %d Invalid SALARY(S)",total_invalid_salary)

    # ===============Invalid Joining Date
    logger.info("Checking Joining Date Validation")

    total_invalid_joining_date=find_invalid_joining_date(employees)
    if total_invalid_joining_date==0:
            logger.info("No Invalid Joining Date Found")
    else:
        logger.warning("Found %d Invalid DATE(S)",total_invalid_joining_date)


    # count_missing_first_name=find_missing_first_name(employees)
    # column_name=input("Enter column name...\n The options you have is : id | first_name | last_name | email | gender | country | joining_date | salary | department | age ")
   
    # ==================Styling console report================ #
    # print(employees)
    print("="*30 )
    print("Data Quality Check")
    print("="*30 )

    print("Dataset Summary")
    print("-"*30 )
    

    # ============Total_ROWS & Total_COLUMNS============= #
    print(f"Total rows present in the current DataSet is : {total_rows:<25}")
    print(f"Total columns present in the current DataSet is : {total_columns:<20}")


    # ============MISSING_COLUMNS============= #
    missing_columns= [
        "first_name","last_name","email","gender","joining_date","department"
        # add the name of columne you want to check out 
    ]
    print("-"*30 )
    for missing_column in missing_columns:
        logger.info("Checking missing values in column: %s", missing_column)

        column_missing_values =find_missing_values(employees,missing_column )
        print(f"Missing values in {missing_column:<20} is {column_missing_values:<20}")
        if column_missing_values==0:
            logger.info("No Missing values in %s : " , missing_column)
        else:
            logger.warning("Missing values in %s : %d " , missing_column, column_missing_values)

    # print(f"Count of Missing First Name  : {count_missing_first_name}")
    # print(f"Count of missing values in {column_name} is {column_missing_values}")
    
    print(f"Invalid emails {total_invalid_emails} ")

    print(f"Invalid age {total_invalid_age} ")
    print(f"Invalid salary {total_invalid_salary} ")
    print(f"Invalid Joining Date {total_invalid_joining_date} ")
    

    # ==========Duplicate items================ #

    column_name= [
            "first_name","last_name","email","joining_date","department"
            # add the name of columne you want to check out 
        ]
    

    for duplicate_column in  column_name:
        logger.info("Checking Duplicate values in column: %s", duplicate_column)
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
        
        if duplicate_items_found ==0:
            logger.info("No Duplicate values found in : %s " , duplicate_column)

        else:
            logger.warning("Found %d   duplicate value(s) in column  %s ", duplicate_items_found, duplicate_column )



            
            # total_invalid_column_details, count_seen_for_every_duplicate=find_duplicate_values(employees,column_name)
            # print(f"Count of duplicate data in : {column_name}\n duplicate occurence : {total_invalid_column_details}\n and the duplicate values are : {count_seen_for_every_duplicate}")
    
    #===============gnerating report==================#
    generate_report(
        employees,
    total_rows,
    total_columns,
    total_invalid_emails,
    total_invalid_age,
    total_invalid_salary,
    total_invalid_joining_date
    )
    logger.info("Data Quality Auditor completed successfully."
)




main()

